from setuptools import find_packages, setup

package_name = 'weather_info_pkg'  # パッケージ名を更新

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'requests'],  # requestsライブラリを追加
    zip_safe=True,
    maintainer='kazu0709',
    maintainer_email='s23C1033WD@s.chibakoudai.jp',
    description='A ROS 2 package for publishing weather information',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = weather_info_pkg.talker:main'  # 実行エントリーポイント  
            #'listener = weather_info_pkg.talker:main'
        ],
    },
)

