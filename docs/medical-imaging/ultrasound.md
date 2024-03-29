---
authors:
    - zyc
date: 2020-03-10 00:14:15
categories:
    - BioMedical Imaging
tags:
    - BioMedical Imaging
---

# 超声成像

!!! abstract ""

    超声影像设备由于其成本低廉、安全快速、体瘦身轻等诸多优点，是四大医学影像设备当中装机量最大、使用最广泛的。

    超声影像设备的基本原理与超声波的物理特性及人体组织对入射超声波所产生的多种物理现象有关。

## 超声波

众所周知，声音是一种压力波，所以其也被称为声波。声音的频率即为压力波变化的周期。由于流体中不存在剪切模量，因此超声影像设备主要依靠纵波。

一般而言，频率介于20Hz与20kHz之间的声音可以被人类所听到。因此，我们将频率低于20Hz的声波称为次声波，将频率超过20kHz的声波称为超声波。

### 物理特性

超声波具有所有波所具有的物理特性，这包括：

1. **反射** 超声波入射到比自身波长更大的界面时，声波的较大部分能量被该界面阻挡而返回。
2. **折射** 由于人体各组织脏器中的声速不同，声束在经过这些组织间的大界面时会产生声束前进方向的改变。折射可是测量及导向两个方面产生误差。
3. **散射** 小界面对入射超声产生散射现象，使入射超声的部分能量向各个空间方向分散辐射。散射回声来自脏器内部的细小结构，其临床意义十分重要。
4. **衍射** 声束在界面边缘经过时可向界面边缘靠近儿绕行，产生声轴的弧形转向。
5. **相干** 两束声波在同一空间传播时会产生叠加。
6. **多普勒效应** 当一定频率的超声波在介质中传播时，如遇到与声源做相对运动的界面，则其反射的超声波频率随界面运动的情况而发生改变。界面朝向探头运动时反射频率增高，背离界面运动时反射频率降低。
7. **衰减** 超声波在介质中传播时，由于以上提到的反射、散射等其他特性以及声束的扩散和介质对能量的吸收等因素，声能逐渐减少。不同组织对超声能量的吸收能力不同，这主要与其所含的蛋白质和水有关。在人体组织中，声能衰减程度依次序递减为：骨质与钙质、肝脾等实质组织、脂肪组织、液体。超声通过骨质与钙质时明显衰减导致其后方回声减弱乃至消失，从而形成声影（acoustic shadow），但在通过液体时几乎不衰减。

此外，与普通的声波不同，超声波还具有如下性质：

1. **指向性** 由于超声波频率高波长短，因此其具有良好的指向性。这是超声检查对人体器官结构进行探测的基础。

### 实用特性

+ 非侵入性
+ 安全
+ 快速
+ 偏移
+ 低分辨率

## 组织

+ 胎儿
+ 心脏
+ 动脉

## 成像原理

入射超声波在人体组织中传播，当其经过不同的组织、器官，包括正常与病变组织的多层界面时，每一界面由于两侧介质的声阻抗不同而发生不同程度的反射和/或散射。这些反射和/或散射形成的回声，以及超声在传播过程中所经过不同组织的衰减信息，经接受、放大和信息处理而形成声像图（ultrasonogram/echogram）。

超声波假设物体一定不会吸收全部的声波，也即物体一定会反射一定量的声波。

impedance must match
without the matching impedance at the tissue layer, not enough acoustic wave frequency transmitted into the tissue
all tissue have certain amount of compressibility
leads to density

### 声压

对于声压$p$，特性阻抗$Z$与粒子速度$c$，我们有。

$$p = Zv$$

这个式子与初中电学欧姆定律的内容很相似--电压=电阻*电流。其中，

$$Z = \rho c$$

$\rho$为密度。又因为对于压缩系数$k$，我们有$c = \sqrt{\frac{1}{k \rho}}$，上式也可以简化为

$$Z = \sqrt{\frac{\rho}{k}}$$

## 类型

超声成像根据原理可以分为A、B、M、D四种型号，其中D型又有多种子型号用以观察血流状况与组织运动。

### A型超声

A型超声的声像图为一维波形图。其中，横坐标为超声的传播和反射时间，纵坐标则为反射波幅。界面两侧介质的声阻抗之差越大，回声的波幅越大。

**现时，A型超声已经基本没有应用。**

### B型超声

B型超声采用多个声束对选定切面进行检查，并将每条声束的所有回声依各自的回声时间（代表回声深度）和强弱，重新组成检查切面的二维图像。其中，图像上的纵坐标代表回声时间，而回声的强弱则用不同辉度的光点来表示。

### M型超声

M型超声采用单个声束对选定切面进行检查，但其在横坐标方向加入一对慢扫描波，使回声光点沿水平方向移动从而得到选定切面不同深度组织回声随时间变化的曲线。M型超声与B型超声的声像图没有本质区别，他们的区别在于使用不同的方式以得到回声时间。

!!! info

    B型超声与M型超声的声像图都为二维声像图。在二维声像图上，依据组织内部声阻抗及声阻抗差的大小，可以将人体组织器官分为四种类型：

    | 反射类型 	| 二维超声 	| 图像表现           	| 组织器官                             	|
    |:--------:	|----------	|--------------------	|--------------------------------------	|
    |  无反射  	| 液性暗区 	| 无回声             	| 血液、尿液、胆汁、囊液等液体         	|
    |  少反射  	| 低亮度   	| 低回声             	| 心、肝、胰、脾等实质器官             	|
    |  多反射  	| 高亮度   	| 高回声             	| 血管壁、心瓣膜、脏器包膜、组织纤维化 	|
    |  全反射  	| 极高亮度 	| 强回声，后方有声影 	| 骨骼、钙斑、结石、含气肺、含气肠管   	|

### D型超声

D型超声及多普勒超声，这包括频谱多普勒超声、彩色多普勒血流成像（Doppler Color Flow Imaging, DCFI）等，可以对人体的血流及组织运动的方向、速度等进行观察。

多普勒效应是指如果物体发生运动，则频率会发生变化。

红细胞有很强的粘性，并且对声音有很好的反射。如果血液向换能器移动，那么反射频率将会升高，反之则会降低。

#### 频谱多普勒超声

频谱多普勒超声是根据多普勒效应，提取超声声束在传播途径中各个活动界面所产生的频移即差频回声。图像以频谱方式显示，其中纵坐标表示差频的数值（以速度表示），横坐标代表时间。朝向探头侧的差频信号位于基线上方，而背向探头者则在基线下方。频谱多普勒包括脉冲多普勒、连续多普勒和高脉冲重复频率多普勒，以前两者常用。脉冲多普勒采用单个换能器，利用发射与反射的间隙接收频移信号，具有距离选通功能，可定位分析，但不能准确测量高速血流。连续多普勒采用两组换能器，分别发射超声波和接收其反射波，可用于高速血流的定量分析，但无距离选通功能。

频谱型多普勒超声检查能够获取组织和器官结构及病变的血流信息，包括血流方向、速度、性质、压力阶差等，可对心脏、血管和脏器病变的血流进行定性和定量分析。

#### 彩色多普勒血流成像(DCFI)

彩色多普勒血流成像是利用多普勒效应，提取二维切面内所有差频回声，以彩色方式显示，并叠加在相匹配的二维声像图上。在DCFI图像上，以红、蓝、绿三色表示血流多普勒差频回声，其中朝向探头的血流以红色表示，背向探头者以蓝色表示，湍流方向复杂、多变，呈五彩镶嵌或绿 色。血流速度快者，色彩鲜亮，慢者则暗淡。

彩色多普勒血流成像够直观显示心脏、血管和脏器的血流状况，通过色彩改变可敏感地发现异常血流，但不能进行精确的定量分析。

#### 彩色多普勒能量图(COE)

DCFI能反映血流速度、加速度和方向变化，但这些信息受探测角度的影响较大，且检测低速血流的能力受限。而彩色多普勒能量图(color Doppler energy , CDE)提取和显示多普勒信号的能量信号强度，成像参数为血流中与散射相对应的能量信号，主要取决于取样中红细胞相对数量的多少。能显示低速血流而不受探测角度因素的影响，也不存在彩色混叠现象。组织多普勒成像(tissue Doppler ima­ging , TDI)是以多普勒原理为基础，利用血流滤波器滤去低幅高频（血流）信息，仅检测心室壁反射回 来的低频高振幅频移信号，从而显示心肌组织的运动情况。

彩色多普勒能量图显示信号的动态范围广，能有效显示低速血流，对末梢血流、肿瘤滋养血管和某些部位血流灌注提供重要信息。
4组织多普勒成像(TOI)通过特殊方法提取心肌运动所产生的多普勒频移信号进行分析、处理和成像 ，可对心肌运动进行定性和定量分析。
