### install
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essentials cmake unzip pkg-config
sudo apt-get install python3.6-dev\
sudo apt-get install libatlas-base-dev gfortran\
sudo add-apt-repository “deb http://security.ubuntu.com/ubuntu xenial-security main”
sudo apt update
sudo apt-get install libjasper1 libjasper-devsudo apt-get install libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk-3-dev
wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.4.zip\
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.4.zip\
unzip opencv.zip opencv\
unzip opencv_contrib.zip\
mv opencv-3.4.4/ opencv\
mv opencv_contrib-3.4.4/ contrib\
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/get-pip.py ~/.cache/pip
sudo echo export "WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh">> ~/.bashrc\
source ~/.bashrc\
mkvirtualenv cv -p python3\
workon cv\
cd opencv\
mkdir build\
cd build\
cmake -D CMAKE_BUILD_TYPE=RELEASE     -D CMAKE_INSTALL_PREFIX=/usr/local     -D WITH_CUDA=OFF     -D INSTALL_PYTHON_EXAMPLES=ON     -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules  -D ENABLE_PRECOMPILED_HEADERS=OFF     -D OPENCV_ENABLE_NONFREE=ON     -D BUILD_EXAMPLES=ON ..\
make -j4
sudo ldconfig
sudo make install
pkg-config --modversion opencv
cd ~/.virtualenvs/cv/lib/python3.6/site-packages/
ln -s /usr/local/python/cv2/python-3.6/cv2.so cv2.so
sudo ldconfig\
pkg-config --modversion opencv\
ld /usr/local/python/cv2/python-3.6\
sudo mv cv2.cpython-36m-x86_64-linux-gnu.so cv2.so\
pip install imutils\
pip install scikit\
pip install scipy\
pip install plotly\
pip install inquirer\
pip install numpy\
pip install urllib\
pip install dlib\

