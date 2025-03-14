from PyQt6 import uic
from PyQt6.QtWidgets import QTreeWidgetItem, QWidget, QTreeWidget, QApplication
from PyQt6.QtGui import QIcon, QColor
from PyQt6.QtCore import QEvent, Qt, pyqtSignal, QModelIndex
from m3u_parser import M3uParser
from AppData import * 
import tempfile
import re
import json
import requests
import os
 

PLAYLIST_COLOR = QColor(20, 6, 36)   #QColor(20, 6, 36)
LIBRARY_COLOR = QColor(20, 6, 36)
FAVORITES_COLOR = QColor(20, 6, 36)
SEARCH_COLOR = QColor(20, 6, 36)  #QColor(0, 35, 63)
SESSION_COLOR = QColor(39, 0, 42) #QColor(0, 35, 63)

def pad(string: str) -> str:
    return "  " + string



class TreeItem(QTreeWidgetItem):
    def __init__(self, nameText, bgColor:QColor = None, isPlayList: bool = False, isPersistent: bool = True):
        super().__init__([nameText])
        self.itemName = nameText.lstrip()
        self.playListName = ""
        self.isPlayList = isPlayList
        self.isPersistent = isPersistent
        
        if bgColor != None:
            self.setBackground(0, bgColor)
        
    def SetPlayListName(self, name: str):
        self.playListName = name
        
    def GetPlayListName(self) -> str:
        return self.playListName
    
    def GetItemName(self) -> str:
        return self.itemName
    
    def SetSource(self, source: str):
        self.setData(0, Qt.ItemDataRole.UserRole, source)
        
    def GetSource(self) -> str:
        return self.data(0, Qt.ItemDataRole.UserRole)
    
    def SetItemChecked(self, checked: bool):
        if checked:
            self.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.setCheckState(0, Qt.CheckState.Unchecked)
            
    def IsItemChecked(self) -> bool:
        return self.checkState(0) == Qt.CheckState.Checked
    
    def IsItemPersistent(self) -> bool:
        return self.isPersistent
    
    def GetParentName(self) -> str:
        parent = self.parent().text(0)
        parent = parent.split("  (")[0]
        parent = parent.lstrip()
        return parent
        
        
class PlayListManager(QWidget):
    platform: str = ""
    treeItemSelectedSignal: pyqtSignal = pyqtSignal(str, str)
    currentSelectedItem: TreeItem = None
    lastSelectedItem: TreeItem = None
    searchResultsCount = 0
    currentItem = 0
    openedFilesList: TreeItem = None
    openedSessionPlayLists: List[PlayListEntry] = []
    openedSessionFiles: List[PlayListEntry] = []
    
    def __init__(self, playlistTreefromUI: QTreeWidget, appData: AppData, parent=None):
        super().__init__(parent)
        
        self.platform = parent.platform
        
        print("Platform: " + self.platform)
        
        # Setup The Playlist Tree
        self.playlistTree = playlistTreefromUI
        self.playlistTree.setColumnCount(1)
        
        # Setup AppData
        self.appData = appData
        
        # Load Custom Stylesheet
        self.playlistTree.setStyleSheet(self.LoadStyleSheet())
        self.setMouseTracking(True)
        self.lower()
        
        # Add core Playlists
        self.ResetAllLists()
        
        # Setup Event Handlers
        #self.installEventFilter(self)
        self.playlistTree.installEventFilter(self)
        self.playlistTree.itemDoubleClicked.connect(self.ItemDoubleClicked)
        self.playlistTree.itemClicked.connect(self.ItemClicked)
        self.playlistTree.itemChanged.connect(self.ChannelCheckBoxChanged)
        
        
    def ResetAllLists(self):
        self.playlistTree.clear()
        
        # Add core Playlists
        self.searchList = TreeItem(pad("Search Results"), SEARCH_COLOR, True)
        self.searchList.setIcon(0, QIcon(":icons/icons/search-list.png"))
        
        self.favoritesList = TreeItem(pad("Favorites"), FAVORITES_COLOR, True)
        self.favoritesList.setIcon(0, QIcon(":icons/icons/star-white.png"))
        
        self.libraryList = TreeItem(pad("Library"), LIBRARY_COLOR, True)
        self.libraryList.setIcon(0, QIcon(":icons/icons/library.png"))
        
        self.AppendPlayList(self.searchList)
        self.AppendPlayList(self.favoritesList)
        self.AppendPlayList(self.libraryList)

        self.openedFilesList = None
        self.currentSelectedItem = None
        self.lastSelectedItem = None
        
        
    def ReAddOpenFilesList(self):            
        if len(self.openedSessionFiles) > 0:
            for item in self.openedSessionFiles:
                self.AddSessionFile(item)
            
    def ReAddOpenSessionPlayLists(self):            
        if len(self.openedSessionPlayLists) > 0:
            for item in self.openedSessionPlayLists:
                self.LoadPlayList(item, False)
                
    def LoadStyleSheet(self):
        iconPath = ":/icons/icons/"
            
        icon_star_full = os.path.join(iconPath, 'star-full.png')
        icon_star_empty = os.path.join(iconPath, 'star-empty.png') 
        icon_collapsed = os.path.join(iconPath, 'collapsed.png')
        icon_expanded = os.path.join(iconPath, 'expanded.png')
        
        
        #color: white;
        #font: 12pt "Arial";
        stylesheet = f"""
        QTreeWidget
        {{
        background-color: rgb(15, 15, 15);
        background: black;
        color: white;
        border-right-color: rgb(30, 30, 30);
        }}

        QTreeView::branch:open
        {{
        image: url("{icon_expanded}");
        }}
        QTreeView::branch:closed:has-children
        {{
        image: url("{icon_collapsed}");
        }}

        QTreeWidget::item
        {{
        height: 50px;
        }}

        QTreeWidget::indicator
        {{
        width: 16px;
        height: 16px;
        }}

        QTreeWidgetItem::indicator:enabled
        {{
        padding-right: 10px;
        }}

        QTreeWidget::indicator:checked
        {{
        image: url("{icon_star_full}");
        }}

        QTreeWidget::indicator:unchecked
        {{
        image: url("{icon_star_empty}");
        }}

        QTreeView::item:selected
        {{
        background-color: rgb(30, 30, 30);
        border: 1px solid black; /*rgb(82, 26, 149);*/
        border-left-color: transparent;
        border-right-color: transparent;
        color: white;
        }}
        
        /*QTreeView::item:unselected
        {{
        border: none;
        color: white;
        }} */  
                
        QTreeView::item:hover
        {{
        background-color: rgb(35, 11, 63);
        border: 1px solid rgb(82, 26, 149);
        border-left-color: transparent;
        border-right-color: transparent;
        color: white;
        }}    
            
        QScrollBar:vertical 
        {{
            border: 1px solid black;
            background: black;
            width: 15px;
            margin: 22px 0 22px 0;
        }}
        QScrollBar::handle:vertical 
        {{
            border: 1px solid rgb(30, 30, 30); /*rgb(35, 11, 63);*/
            background: black; /*rgb(30, 30, 30);*/
            min-height: 40px;
            border-radius: 4px; 
        }}
        QScrollBar::add-line:vertical 
        {{
            border: 1px solid  rgb(30, 30, 30);
            background:  transparent; /*rgb(30, 30, 30); */
            height: 15px;
            border-radius: 4px; 
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }}
        QScrollBar::sub-line:vertical 
        {{
            border: 1px solid  rgb(30, 30, 30);
            background:  transparent; /*rgb(30, 30, 30); */
            height: 15px;
            border-radius: 4px; 
            subcontrol-position: top;
            subcontrol-origin: margin;
        }}  
        background-color: rgb(15, 15, 15);
        border: 1px solid transparent;
        color: white;
        """
        
        #self.playlistTree.setHorizontalScrollMode(QTreeWidget)
        return stylesheet   
    
    def EmitTreeLayoutChanged(self):
        self.playlistTree.model().layoutChanged.emit()  
            
    def AppendPlayList(self, newPlayList: TreeItem, targetItem: TreeItem = None):
        if not newPlayList.isPlayList:
            return
        
        if targetItem is None:
            self.playlistTree.insertTopLevelItem(self.playlistTree.topLevelItemCount(), newPlayList)
        else:
            targetItem.insertChild(targetItem.childCount(), newPlayList) 
    
    
    def AppendChannel(self, playList: TreeItem, newChannel: TreeItem):
        if not newChannel.isPlayList:
            playList.insertChild(playList.childCount(), newChannel)
    
        
    def UpdatePlayListChannelCount(self, item: TreeItem, count: int = -1):
        if count == -1:
            count = item.childCount()
        
        if item.isPlayList:
            item.setText(0, pad(item.GetItemName()) + "  (" + str(count) + ")")
                
    def CollapseAllPlaylists(self):
        self.playlistTree.collapseAll()
        
    def ExpandAllPlaylists(self):
        self.playlistTree.expandAll()
                       
    def LoadPlayList(self, playlist: PlayListEntry, isPersistent: bool = True):        
        # Extract the file name without the extension
        playlistPath = playlist.source
        #playListFile = os.path.basename(playlistPath)

        #playlistName, extension = os.path.splitext(os.path.basename(playListFile))
        playlistName = playlist.name
        # Initialize the parser
        parser = M3uParser()
        
        #-----------------------------------------------
        # Attemp to fetch and parse a remote playlist
        #-----------------------------------------------
        if playlistPath.startswith("http"):
            try:
                response = requests.get(playlistPath)
                
                # Create a temporary file
                with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.m3u', encoding='utf-8') as temp_file:
                    # Write the content to the temporary file
                    temp_file.write(response.text)
                    responseFile = temp_file.name
        
                parser.parse_m3u(responseFile, check_live=False)
                os.remove(responseFile)
            except requests.exceptions.RequestException as e:
                print(f"Error fetching remote playlist: {e}")
                return
        #----------------------------------------
        # Attempt to parse local playlist file   
        #---------------------------------------- 
        else:
            # Verify that the playlistPath exists, then parse the file
            if os.path.exists(playlistPath):
                parser.parse_m3u(playlistPath, check_live=False)
            else:
                print("The playlist file does not exist.")
                return

        #------------------------------
        # Check if the parser is empty
        #------------------------------
        entries = parser.get_list()
        if not entries:
            print("The playlist is empty.")
            return
        
        self.playlistTree.blockSignals(True)
        if isPersistent:
            # Create a Playlist Entry to the Tree and add it 
            playlistTreeItem = TreeItem(pad(playlistName), PLAYLIST_COLOR, True)
            self.AppendPlayList(playlistTreeItem)
        else:
            playlistTreeItem = TreeItem(pad(playlistName), SESSION_COLOR, True, False)
            if not self.IsEntryInSessionPlayList(playlist):
                self.openedSessionPlayLists.append(playlist)
            self.AppendPlayList(playlistTreeItem)
                
        #------------------------------
        # Process the parsed entries
        #------------------------------
        for entry in entries:
            channel_name = entry.get('name', 'Unknown') # Get the title from the EXTINF tag
            source = entry.get('url', 'No URL')  # Get the stream URL or file path
            
            if channel_name and source:
                # Create a new item for the channel and add it as a child to the playlist item
                channelItem = TreeItem(pad(channel_name), None, False, isPersistent)
                channelItem.SetPlayListName(playlistName) 
                channelItem.SetSource(source)

                if isPersistent:
                    channelItem.setFlags(channelItem.flags() | Qt.ItemFlag.ItemIsUserCheckable) 
                    channelItem.SetItemChecked(False)
                
                self.AppendChannel(playlistTreeItem, channelItem) 
                
        # Rename the playlist item
        self.UpdatePlayListChannelCount(playlistTreeItem)
        self.playlistTree.blockSignals(False)
        
    def AddSessionFile(self, fileEntry: PlayListEntry):
        if fileEntry is None:
            return
        
        self.playlistTree.blockSignals(True)  
        # If not files have been opened yet, create the root item
        if self.openedFilesList is None:
            self.openedFilesList = TreeItem(pad("Opened Files"), SESSION_COLOR, True, False)
            self.AppendPlayList(self.openedFilesList)
            
        item = TreeItem(pad(fileEntry.name), None, False, False)
        item.SetSource(fileEntry.source)
        item.SetPlayListName("Opened Files")
        
        self.AppendChannel(self.openedFilesList, item)
        self.UpdatePlayListChannelCount(self.openedFilesList)
        
        if not self.IsEntryInSessionFiles(fileEntry):
            self.openedSessionFiles.append(fileEntry)
            
        self.playlistTree.blockSignals(False)  
        #self.openedFilesList.setSelected(True)
        #self.EmitTreeLayoutChanged()
            
    def ItemDoubleClicked(self, item: TreeItem, column):
        # If item is a playlist, return
        if item.isPlayList:
            return
        
        temp = self.currentSelectedItem
        
        channel_name = item.GetItemName()
        source = item.GetSource()
        
        # Check if selection is from Search List, if so Find the Channel from the Tree
        if item.playListName == self.searchList.GetItemName():
            # Get the playlist name that item is in listed in the search list
            play_list_name = item.GetParentName()
            
            # Get the real channel from the tree
            item = self.GetChannelFromTree(play_list_name, channel_name, source)
        
        self.currentSelectedItem = item
        
        self.lastSelectedItem = temp
        self.playlistTree.setFocus()
        self.treeItemSelectedSignal.emit(channel_name, source)
        
    def ItemClicked(self, item: TreeItem):
        if item is None:
            return
        
        # Expand a Playlist if selected
        if item.isPlayList:
            self.playlistTree.setFocus()
            item.setExpanded(not item.isExpanded())
            return
        
    def ItemManuallyEntered(self):
        selectedItem = self.playlistTree.currentItem()
        
        if selectedItem.isPlayList:
            selectedItem.setExpanded(not selectedItem.isExpanded())
            return
        
        self.ItemDoubleClicked(selectedItem, -1)
        
    def GetChannelFromTree(self, playListName, channelName, source):
        # Index through the Playlists of the tree
        for row in range(self.playlistTree.topLevelItemCount()):
            item = self.playlistTree.topLevelItem(row)
            
            # Exclude the Search List and Favorites List
            if item.GetItemName() == self.searchList.GetItemName(): # or item.GetItemName() == self.favoritesList.GetItemName():
                continue
            
            # If Playlist is found, then index through the channels of the playlist
            if item.GetItemName() == playListName:
                for childRow in range(item.childCount()):
                    child = item.child(childRow)
                    if child.GetItemName() == channelName and child.GetSource() == source:
                        return child
        return None
    
    def GetPlayListFromTree(self, playListName) -> TreeItem:
        for row in range(self.playlistTree.topLevelItemCount()):
            item = self.playlistTree.topLevelItem(row)
            if item.GetItemName() == playListName:
                return item
        return None
    
    def GetPlayListFromSearch(self, playListName) -> TreeItem:
        if self.searchList.childCount() == 0:
            return None
        
        for row in range(self.searchList.childCount()):
            item = self.searchList.child(row)
            if item.GetItemName() == playListName:
                return item
        return None
        
    def ClearPlayListItems(self, playList: TreeItem):
        if not playList.isPlayList:
            return
        
        while playList.childCount() > 0:
            child = playList.child(0)
            playList.removeChild(child)
    
    
    def GoToLastSelectedItem(self):
        if self.lastSelectedItem is None:
            return None, None
        
        temp = self.currentSelectedItem
        self.currentSelectedItem = self.lastSelectedItem
        self.lastSelectedItem = temp
        
        # Retrieve the channel name (displayed)
        channel_name = self.currentSelectedItem.GetItemName()

        # Retrieve the hidden URL (stored in UserRole)
        source = self.currentSelectedItem.GetSource()
        
        # Set Tree to Selected Item
        self.playlistTree.setCurrentItem(self.currentSelectedItem)
        
        return channel_name, source
    
    def GoToAdjacentItem(self, isForward: bool = True):
        if self.currentSelectedItem is None or self.currentSelectedItem.isPlayList:
            return None, None
        
        temp = self.currentSelectedItem
        
        # Check if selection is from Search List, if so goto next item in that list 
        if self.currentSelectedItem.parent().parent() == self.searchList:     
            currentList = self.GetPlayListFromSearch(self.currentSelectedItem.GetPlayListName())
        else:
            currentList = self.currentSelectedItem.parent()  
                    
        currentListCount = currentList.childCount()
        currentIndex = currentList.indexOfChild(self.currentSelectedItem)
        
        if isForward:
            nextItemIndex = (currentIndex + 1) % currentListCount
        else:
            nextItemIndex = (currentIndex - 1) % currentListCount
        
        self.currentSelectedItem = currentList.child(nextItemIndex)
        
        self.lastSelectedItem = temp
        
        # Retrieve the channel name (displayed)
        channel_name = self.currentSelectedItem.GetItemName()

        # Retrieve the hidden URL (stored in UserRole)
        source = self.currentSelectedItem.GetSource()
        
        # Set Tree to Selected Item
        self.playlistTree.setCurrentItem(self.currentSelectedItem)
        
        return channel_name, source
    
    def SaveFavorites(self):
        self.appData.save()
            
    def LoadFavorites(self):
        self.playlistTree.blockSignals(True)  
        self.ClearPlayListItems(self.favoritesList)        

        # Find Corresponding Playlist Items
        for item in self.appData.Favorites:  #self.favoritesInfo:
            # Find the item.playListName in the tree
            favoriteItem = self.GetChannelFromTree(item.parentName, item.name, item.source)  
            
            # If item is found, check it
            if favoriteItem:
                favoriteItem.SetItemChecked(True)
            else:
                continue
                
            #print("Loaded favorite: " + item['channelName'] + " from " + item['playListName'] + " playlist" + " from " + item['source'])
            
            # Add the item to the favorites list
            newEntry = TreeItem(favoriteItem.GetItemName())
            newEntry.SetPlayListName(favoriteItem.GetPlayListName())     #GetParentName())  
            newEntry.SetSource(favoriteItem.GetSource())

            newEntry.setFlags(newEntry.flags() | Qt.ItemFlag.ItemIsUserCheckable) 
            newEntry.SetItemChecked(True)
            
            # Add the item to the favorites list
            self.AppendChannel(self.favoritesList, newEntry)
            
              
        self.UpdatePlayListChannelCount(self.favoritesList)    
        self.playlistTree.blockSignals(False)
             
        print("Favorites loaded successfully")
        
    def LoadLibrary(self):
        self.ClearPlayListItems(self.libraryList)
        
        for item in self.appData.Library:
            newEntry = TreeItem(item.name)
            newEntry.SetPlayListName("Library")
            newEntry.SetSource(item.source)
            
            newEntry.setFlags(newEntry.flags() | Qt.ItemFlag.ItemIsUserCheckable) 
            newEntry.SetItemChecked(False)
            
            # Add the item to the library list
            self.AppendChannel(self.libraryList, newEntry)
            
        self.UpdatePlayListChannelCount(self.libraryList) 
        
    def ToggleItemCheckedinList(self, playList: TreeItem, item: TreeItem, checked: bool):
        if item is None or playList is None:
            return
        
        channelName = item.GetItemName()
        channelSource = item.GetSource()
        
        # Search Playlist for corresponding channel
        for i in range(playList.childCount()):
            child = playList.child(i)
            if child.GetItemName() == channelName and child.GetSource() == channelSource:
                # If channel is found, uncheck it
                child.SetItemChecked(checked)
                break   
        
        
    def ChannelCheckBoxChanged(self, item: TreeItem, column):
        if item is None:
            return
        
        if item.IsItemChecked() == True:
            
            channelName = item.GetItemName()
            channelSource = item.GetSource()
            channelPlaylist = item.GetParentName()
            print("NEW ChannelName: " + channelName + " Source: " + channelSource + " Playlist: " + channelPlaylist)
            
            # Check if item is already in favorites list
            for i in range(self.favoritesList.childCount()):
                favItem = self.favoritesList.child(i)
                if favItem.GetItemName() == channelName and favItem.GetSource() == channelSource:
                    print("Item already in favorites list")
                    return
                      
            # item is not in favorites list, then proceed to add it
            self.playlistTree.blockSignals(True)  
                               
            newFav = TreeItem(channelName)
            newFav.SetPlayListName(channelPlaylist)
            newFav.SetSource(channelSource)
            newFav.setFlags(newFav.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            newFav.SetItemChecked(True)
            
            self.AppendChannel(self.favoritesList, newFav)
            self.UpdatePlayListChannelCount(self.favoritesList)
            
            # Add to favorites info
            isURL = channelSource.startswith("http")
            if isURL:
                sourceType = "url"
            else:
                sourceType = "file"
                
            self.appData.Favorites.append(PlayListEntry(
                name=channelName,
                parentName=channelPlaylist,
                sourceType=sourceType,
                source=channelSource))
                
            self.SaveFavorites()
            
            # Update the Playlist and Search Channel (if Search has been done)
            playlist = self.GetPlayListFromTree(channelPlaylist)
            searchList = self.GetPlayListFromSearch(channelPlaylist)
                
            self.ToggleItemCheckedinList(playlist, item, True)
            self.ToggleItemCheckedinList(searchList, item, True)
            
            self.playlistTree.blockSignals(False)  
            self.EmitTreeLayoutChanged()
            
            
        elif item.IsItemChecked() == False:
            
            channelName = item.GetItemName()
            channelSource = item.GetSource()
            channelPlaylist = item.GetPlayListName()
            
            # Check if Favorites list is empty
            if self.favoritesList.childCount() == 0:
                #print("Favorites list is empty")
                return
            
            self.playlistTree.blockSignals(True)  
            
            #print("ChannelName: " + channelName + " Source: " + channelSource + " Playlist: " + channelPlaylist)
            
            # Remove from favoritsInfo
            for i in range(len(self.appData.Favorites)):
                favItem = self.appData.Favorites[i]
                
                if favItem.name == channelName and favItem.parentName == channelPlaylist and favItem.source == channelSource:
                    self.appData.Favorites.pop(i)
                    self.SaveFavorites() 
                    self.LoadFavorites() 
                    
                    # Deselect item from corresponding playlist
                    playlist = self.GetPlayListFromTree(channelPlaylist)
                    
                    # Search Playlist corresponding channel
                    self.ToggleItemCheckedinList(playlist, item, False)
                    
                    # Rerun the search if search results > 0
                    if self.searchList.childCount() > 0:
                        self.SearchChannels(self.lastSearchQuery)
                        
                    else:
                        self.playlistTree.blockSignals(False)
                        self.EmitTreeLayoutChanged()
                    break
                  
            
    
    def SearchChannels(self, searchText: str):
        # Return if search text is empty
        if not searchText:
            return
        self.lastSearchQuery = searchText
        searchText = searchText.lower()
        searchText = searchText.split('+')
        
        self.playlistTree.blockSignals(True)
        
        # Clear the search list 
        self.ClearPlayListItems(self.searchList)
        
        searchResultsCount = 0
        
        # Traverse (playlists) but ignore the Search Playlist
        for row in range(1,self.playlistTree.topLevelItemCount()):
            # Get the playlist item from tree
            playlistToSearch = self.playlistTree.topLevelItem(row)
            
            # Create new playlist to show results
            playlistResults = TreeItem(playlistToSearch.GetItemName(), None, True)
            
            # Treaverse the Playlist and search for channels
            for i in range(playlistToSearch.childCount()):
                channel = playlistToSearch.child(i)
                
                channelName = channel.GetItemName().lower()
                
                # Search the channel name for seach query
                for searchItem in searchText:
                    searchIndex = channelName.find(searchItem.strip())
                    if searchIndex < 0:
                        break;
                
                # If query is found
                if searchIndex >= 0:
                    # Create a new Item to add to results
                    foundChannel = TreeItem(channel.GetItemName())
                    foundChannel.SetSource(channel.GetSource())
                    foundChannel.SetPlayListName(channel.GetPlayListName())
                    
                    if channel.IsItemPersistent():
                        foundChannel.setFlags(foundChannel.flags() | Qt.ItemFlag.ItemIsUserCheckable)
                        foundChannel.SetItemChecked(channel.IsItemChecked())
                    
                    self.AppendChannel(playlistResults, foundChannel)
                    searchResultsCount += 1
                    
            self.UpdatePlayListChannelCount(playlistResults)
            if playlistResults.childCount() > 0:
                self.AppendPlayList(playlistResults, self.searchList)
            
        self.UpdatePlayListChannelCount(self.searchList, searchResultsCount)
        self.playlistTree.blockSignals(False)
        self.playlistTree.setCurrentItem(self.searchList)
        self.searchList.setExpanded(True)
        self.EmitTreeLayoutChanged()
        
    def SortSearchResultsDescending(self):
        for i in range(self.searchList.childCount()):
            searchList = self.searchList.child(i)
            searchList.sortChildren(0, Qt.SortOrder.DescendingOrder)
            
    def SortSearchResultsAscending(self):
        for i in range(self.searchList.childCount()):
            searchList = self.searchList.child(i)     
            searchList.sortChildren(0, Qt.SortOrder.AscendingOrder)
                    
    def SortListDescending(self):
        selectedItem = self.playlistTree.currentItem()
        if selectedItem is None:
            return
        if selectedItem.isPlayList:
            selectedItem.sortChildren(0, Qt.SortOrder.DescendingOrder)
        else:
            playlist = selectedItem.parent()
            playlist.sortChildren(0, Qt.SortOrder.DescendingOrder)
            
    def SortListAscending(self):
        selectedItem = self.playlistTree.currentItem()
        if selectedItem is None:
            return
        if selectedItem.isPlayList:
            selectedItem.sortChildren(0, Qt.SortOrder.AscendingOrder)
        else:
            playlist = selectedItem.parent()
            playlist.sortChildren(0, Qt.SortOrder.AscendingOrder)
            
    def GotoBottomOfList(self):
        selectedItem = self.playlistTree.currentItem()
        
        if selectedItem and not selectedItem.isPlayList:
            playlist = selectedItem.parent()
            
            bottomItem = playlist.child(playlist.childCount()-1)
            self.playlistTree.setCurrentItem(bottomItem)
            
    def GotoTopOfList(self):
        selectedItem = self.playlistTree.currentItem()
        
        if selectedItem and not selectedItem.isPlayList:
            playlist = selectedItem.parent()
            
            topItem = playlist.child(0)
            self.playlistTree.setCurrentItem(topItem)   
           
    def IsEntryInSessionPlayList(self, entry):
        for item in self.openedSessionPlayLists:
            if item.name == entry.name:
                return True
        return False
    
    def IsEntryInSessionFiles(self, entry):
        for item in self.openedSessionFiles:
            if item.name == entry.name:
                return True
        return False
               
    def eventFilter(self, obj, event):
        if obj == self.playlistTree and event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Space:
                return True
            #elif event.key() == Qt.Key.Key_M:
                #self.parent().MutePlayer()
                
        #QApplication.sendEvent(self.parent(), event)
        return super().eventFilter(obj, event)
            
        