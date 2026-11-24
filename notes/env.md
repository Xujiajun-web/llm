(llm) C:\Users\X>nvidia-smi
Tue Nov 24 11:57:24 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 616.92                 KMD Version: 616.92        CUDA UMD Version: 13.4     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                  Driver-Model | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4070 Ti   WDDM  |   00000000:01:00.0 Off |                  N/A |
|  0%   55C    P0             55W /  285W |    3286MiB /  12282MiB |     10%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            4984    C+G   C:\Windows\explorer.exe               N/A      |
|    0   N/A  N/A           12472    C+G   ....0.4341.60\msedgewebview2.exe      N/A      |
|    0   N/A  N/A           13248    C+G   ...IA app\CEF\NVIDIA Overlay.exe      N/A      |
|    0   N/A  N/A           16868    C+G   ...h_cw5n1h2txyewy\SearchApp.exe      N/A      |
|    0   N/A  N/A           17784    C+G   ..._main\CefView\CefViewWing.exe      N/A      |
|    0   N/A  N/A           17980    C+G   ...ypervisor\MuMuVMMHeadless.exe      N/A      |
|    0   N/A  N/A           18048    C+G   ....189.7530.0\QQLiveService.exe      N/A      |
|    0   N/A  N/A           18152    C+G   E:\ToDesk\ToDesk.exe                  N/A      |
|    0   N/A  N/A           19412    C+G   ...5n1h2txyewy\TextInputHost.exe      N/A      |
|    0   N/A  N/A           20028    C+G   ...8bbwe\PhoneExperienceHost.exe      N/A      |
|    0   N/A  N/A           20128    C+G   ...oginClient\flutter\AweSun.exe      N/A      |
|    0   N/A  N/A           22736    C+G   E:\APP\NAS\RaiDrive.exe               N/A      |
|    0   N/A  N/A           24932    C+G   ...shell\CefView\CefViewWing.exe      N/A      |
|    0   N/A  N/A           26380    C+G   ....0.4341.60\msedgewebview2.exe      N/A      |
|    0   N/A  N/A           28352    C+G   ....0.4341.60\msedgewebview2.exe      N/A      |
|    0   N/A  N/A           31684    C+G   ...IA app\CEF\NVIDIA Overlay.exe      N/A      |
|    0   N/A  N/A           32012    C+G   ...xyewy\ShellExperienceHost.exe      N/A      |
|    0   N/A  N/A           33648    C+G   ...App_cw5n1h2txyewy\LockApp.exe      N/A      |
|    0   N/A  N/A           33808    C+G   E:\APP\WorkBuddy\WorkBuddy.exe        N/A      |
|    0   N/A  N/A           35936    C+G   ...ntrolPanel\SystemSettings.exe      N/A      |
|    0   N/A  N/A           36736    C+G   E:\douyin\douyin.exe                  N/A      |
|    0   N/A  N/A           41864    C+G   ...t\Edge\Application\msedge.exe      N/A      |
+-----------------------------------------------------------------------------------------+

(llm) C:\Users\X>python
Python 3.11.18 | packaged by Anaconda, Inc. | (main, Oct 26 2026, 18:13:29) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> print(torch.__version__)
2.15.0+cu134
>>> print(torch.cuda.is_available())
True
