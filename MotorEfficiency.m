%T = readtable('points.csv');

function ret = MotorEfficiency(RPM,torque)
    p00 =       85.36;
    p10 =   -0.004406;
    p01 =     -0.2588;
    p20 =   3.797e-06;
    p11 =   0.0004744;
    p02 =     0.01083;
    p30 =  -1.928e-09;
    p21 =  -1.306e-07;
    p12 =  -4.173e-06;
    p03 =   -0.000191;
    p40 =   4.758e-13;
    p31 =   1.263e-11;
    p22 =   6.055e-10;
    p13 =   2.415e-08;
    p04 =   1.333e-06;
    p50 =  -4.838e-17;
    p41 =   1.036e-15;
    p32 =  -1.164e-13;
    p23 =   1.444e-12;
    p14 =  -9.625e-11;
    p05 =   -3.18e-09;

    ret = p00 + p10*RPM + p01*torque + p20*RPM^2 + p11*RPM*torque + p02*torque^2 + p30*RPM^3 + p21*RPM^2*torque ...
    + p12*RPM*torque^2 + p03*torque^3 + p40*RPM^4 + p31*RPM^3*torque + p22*RPM^2*torque^2 ...
    + p13*RPM*torque^3 + p04*torque^4 + p50*RPM^5 + p41*RPM^4*torque + p32*RPM^3*torque^2 ...
    + p23*RPM^2*torque^3 + p14*RPM*torque^4 + p05*torque^5;
end