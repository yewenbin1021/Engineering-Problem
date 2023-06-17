%%特征点设计调试文件 
clear;clc;
%%特征点参数
a1=0.21;
a2=-250;
a3=200;
a4=1.0;
a5=0.02;
vd=1500;         g=9.80665;          kv=vd/57.3/g;   
nke=30;

Tdxt=0.006;      ksidxt=0.6;         taodxt=0.0025;
Tnt=0.002;       ksint=0.5;
Txg=0.002;       ksixg=0.5;
%%待设计参数

%数据量
n = 10;
%Tfm=0.1;
Tfm_Range = 0 + 5.*rand(1,n); 
%wn=15;
wn_Range = 0+20.*rand(1,n);
%ksi=0.9;
ksi_Range = 0.5+1.5.*rand(1,n);
%kzn=1;
kzn_Range = 0.5+1.5.*rand(1,n);
%kjs=1;
kjs_Range = 0.5+1.5.*rand(1,n);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
inputs = [0,0,0,0,0];
for i = 1:n
    input = [Tfm_Range(i),wn_Range(i),ksi_Range(i),kzn_Range(i),kjs_Range(i)];
    a = input; 
    inputs = [inputs;a];
end
inputs(1,:) = [];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

x=[a1 a2 a3 a4 a5 kv nke Tdxt ksidxt taodxt Tnt ksint Txg ksixg];  %%函数输入参数
output = [];
% for i = 1:10
    v = inputs(i,:);%%待设计参数向量
    y= FuncAutoPilot(v,x);                                     
    output = [output;y];
% end
%%实际性能
%%时域性能
Tr=y(1);       Sigma=y(2);      Kbh=y(3);
Duop=y(4);     dKst=y(5);       dDuop=y(6);
%%频域性能
MagJsd=y(7);   PhaseJsd=y(8);   W0Jsd=y(9);
MagZn=y(10);   PhaseZn=y(11);   W0Zn=y(12);
xlswrite('Input_J.xlsx',inputs)
xlswrite('Output_j.xlsx',output)


