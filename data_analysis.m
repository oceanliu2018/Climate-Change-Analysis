%% This script will generate plots for the data set, one for between
data=load('new_out.txt');
years=data(1:135,1);
deviations=data(1:135,2);
temps=data(1:135,3)
scatter(years,deviations)
xlabel('Years between 1880-2014')
ylabel('deviations in temperature from base period(Celcius)')
title('Average deviations from 1880-2014')
normresid=149.2073;
R2quadratic=1-normresid.^2/sum((mean(deviations)-deviations).^2)
normresid1=177.6625;
R2linear=1-normresid1.^2/sum((mean(deviations)-deviations).^2)
legend('R2quadratic=0.8726 R2linear=0.8194')
figure()
scatter(years,temps)
xlabel('Years between 1880-2014')
ylabel('average temperatures(Celcius)')
title('Average temperatures between 1880-2014')
legend('R2quadratic=0.8726 R2linear=0.8194')
%% 
data=load('new_out.txt');
years=data(1:70,1);
deviations=data(1:70,2);
figure()
scatter(years,deviations)
xlabel('Years between 1880-2014')
ylabel('deviations in temperature from base period(Celcius)')
title('Average deviations between 1880-1950')
normresid2=88.2675;
R2quadratic=1-normresid2.^2/sum((mean(deviations)-deviations).^2)
normresid3=89.9355;
R2linear=1-normresid2.^2/sum((mean(deviations)-deviations).^2)
legend('R2quadratic=0.6595 R2linear=0.6595')

