clc; clear all; close all;

set_point = 25;                             % Desired temperature
initial_value = 19;                         % Initial temperature

s = tf('s');
k = 12.746;                                 % Gain
T = 190;                                    % Time constant
delay = 10;                                 % Delay
H = k * exp(-s * delay) / (1 + s * T);      % Model

kp = 0.3073;
ki = 0.0035;
kd = 0.0122;
dt = 1.0;

f = fopen("temp_log.txt");
data = textscan(f,'%s');
fclose(f);
temperatures = str2double(data{1}(2:2:end));
figure
plot(temperatures)
hold on
plot(25 * ones(589, 1))
