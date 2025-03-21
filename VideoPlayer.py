import platform
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget
import vlc

from enum import Enum
from abc import abstractmethod


#------------------------------------------------
# Video Player ENUMS
#------------------------------------------------
class ENUM_PLAYER_TYPE(Enum):
    VLC = "VLC"
    QTMEDIA = "QTMEDIA"
    
class ENUM_PLAYER_STATE(Enum):
    IDLE = 0
    LOADING = 1
    PLAYING = 2
    PAUSED = 3
    STOPPED = 4
    STALLED = 5
    ENDED = 6
    ERROR = 7
    
#------------------------------------------------
# Video Player Base Class
#------------------------------------------------
class VideoPlayer(QWidget):
    platform: str = platform.system()
    updatePosition = pyqtSignal(int)
    updateDuration = pyqtSignal(int)
    playerStateChanged = pyqtSignal(ENUM_PLAYER_STATE)
    errorOccured = pyqtSignal(str)
    currentState: ENUM_PLAYER_STATE = ENUM_PLAYER_STATE.IDLE
    mainWindow: QWidget = None
    videoPanel: QWidget = None
    source: str = ""
    duration: int = 0
    position: int = 0
    
    #-----------------------
    # Signal Methods
    #-----------------------
    def UpdatePosition(self, position: int):
        self.updatePosition.emit(position)
    
    def UpdateDuration(self, duration: int):
        self.updateDuration.emit(duration)
        
    def UpdatePlayerState(self, state: ENUM_PLAYER_STATE):
        self.playerStateChanged.emit(state)
    
    def ErrorOccured(self, error: str):
        self.errorOccured.emit(error)
        
    #-----------------------
    # Abstract Methods
    #-----------------------
    @abstractmethod
    def InitPlayer(self):
        pass
    
    @abstractmethod
    def Play(self):
        pass
    
    @abstractmethod
    def Pause(self):
        pass
    
    @abstractmethod
    def Stop(self):
        pass
    
    @abstractmethod
    def SetPosition(self, position: int):
        pass
    
    @abstractmethod
    def GetPosition(self):
        pass
        
    @abstractmethod
    def SetVolume(self, volume: int):
        pass
    
    @abstractmethod
    def GetVolume(self):
        pass
    
    @abstractmethod
    def Mute(self, mute: bool):
        pass
    
    @abstractmethod
    def IsMuted(self):
        pass
    
    @abstractmethod
    def SetVideoSource(self, videoSource: str):
        pass
    
    @abstractmethod
    def RefreshVideoSource(self):
        pass
    
    @abstractmethod
    def GetVideoDuration(self):
        pass
    
    @abstractmethod
    def OnChangingPosition(self, isPlaying: bool):
        pass
    
    @abstractmethod
    def OnChangedPosition(self, isPlaying: bool):
        pass
    
    @abstractmethod
    def ChangeUpdateTimerInterval(self, isFullScreen: bool):
        pass
    
    @abstractmethod
    def GetVideoResolution(self):
        pass
    
    @abstractmethod
    def GetSubtitleTracks(self) -> list:
        return
    
    @abstractmethod
    def SetSubtitleTrack(self, index: int):
        pass