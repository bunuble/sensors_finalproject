%fixed_humidity = zeros(numel(Humidity_Outside),1);
synced_date = datetime([],[],[]);

for i = 1:numel(Date_Outside)
    for j = 1:numel(Date_Inside)
        if Date_Outside(i,1) == Date_Inside(j,1)
            synced_date(j,1) = Date_Inside(j,1);
        end
    end
end



%{
for i = 1:numel(Humidity_Outside)
    if Humidity_Outside(i) < 101
        fixed_humidity(i,1) = Humidity_Outside(i);
        fixed_date(i,1) = Date_Outside(i);
    end  
end


subplot(1,3,1)
plot(Date_Inside,Temp_Inside,Date_Outside,Temp_Outside);
xlabel('Date');
ylabel('Temperature (C)')
title('Temperature Outside vs Inside');
legend('Inside','Outside');
subplot(1,3,2)
plot(Date_Inside,Humidity_Inside,fixed_date,fixed_humidity);
xlabel('Date');
ylabel('Humidity (Percent)');
legend('Inside','Outside');
subplot(1,3,3)
plot()
%}