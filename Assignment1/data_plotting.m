clear
close all

is_count = [2.1000000e+01 2.3000000e+01 4.5000000e+01 8.6000000e+01 1.2000000e+02 2.7800000e+02 4.3900000e+02 9.7400000e+02 1.5220000e+03 3.2250000e+03 7.0920000e+03 1.2509000e+04 2.3888000e+04 4.8089000e+04 9.1004000e+04 1.8468100e+05 3.4745200e+05 6.5945200e+05 1.3496500e+06 2.6732270e+06 5.1958290e+06 9.9425940e+06 1.9770518e+07 3.9616885e+07 7.6236641e+07];

ms_count = [3.30000e+01 4.60000e+01 6.70000e+01 9.50000e+01 1.43000e+02 2.07000e+02 3.13000e+02 4.57000e+02 6.81000e+02 1.00100e+03 1.48100e+03 2.17400e+03 3.19500e+03 4.67100e+03 6.82700e+03 9.96000e+03 1.45130e+04 2.11350e+04 3.06730e+04 4.45780e+04 6.44950e+04 9.35670e+04 1.34983e+05 1.95520e+05 2.81349e+05];

hs_count = [2.20000e+01 3.50000e+01 5.50000e+01 8.10000e+01 1.20000e+02 1.75000e+02 2.80000e+02 4.04000e+02 6.13000e+02 9.13000e+02 1.32000e+03 1.96000e+03 2.90500e+03 4.26000e+03 6.25300e+03 9.17700e+03 1.34380e+04 1.95910e+04 2.84520e+04 4.15380e+04 6.02200e+04 8.76600e+04 1.26707e+05 1.83703e+05 2.65433e+05];

qs_count = [3.40000e+01 4.70000e+01 7.00000e+01 7.90000e+01 1.36000e+02 1.64000e+02 2.83000e+02 4.38000e+02 6.57000e+02 1.04600e+03 1.52400e+03 2.22300e+03 3.04200e+03 4.72600e+03 7.09300e+03 1.06590e+04 1.47900e+04 2.48560e+04 3.53920e+04 4.87950e+04 7.23290e+04 1.02905e+05 1.57491e+05 2.27885e+05 3.42328e+05];

init_datalen = 5;
scale_coef = 1.4;
datalens = zeros(1, 25);
datalens(1) = init_datalen;
datalens(1) = floor(datalens(1)*scale_coef)

if (length(is_count) == length(ms_count)) && ...
   (length(ms_count) == length(hs_count)) && ...
   (length(hs_count) == length(qs_count))

    for i = 2:25
        datalens(i) = floor(datalens(i-1)*scale_coef)

    end
else
    error('Data does not have the same length')
end

% Ensure x_data and y_data are column vectors
datalens = datalens(:);
is_count = is_count(:);

% Construct the design matrix for the quadratic function
% Each row is [x^2, x, 1]
A = [datalens.^2, datalens, ones(size(datalens))];

% Solve the equation A * coeffs = y to get the coefficients
coeffs = A \ is_count;

% Extract coefficients a, b, c
a = coeffs(1);
b = coeffs(2);
c = coeffs(3);

% Display the results
fprintf('The quadratic function is: y = %.4fx^2 + %.4fx + %.4f\n', a, b, c);

figure(1)
hold on
grid on
% use in case of logaritmic axis
% set(gca, 'XScale', 'log')
% set(gca, 'YScale', 'log')

% Plot the data points and the fitted curve
x_fit = linspace(min(datalens), max(datalens), 100);  % Generate smooth x values for plotting
y_fit = a * x_fit.^2 + b * x_fit + c;            % Compute the corresponding y values

plot(datalens, is_count, 'ro', 'MarkerSize', 8, 'DisplayName', 'Data Points'); % Original data points
plot(x_fit, y_fit, 'b-', 'LineWidth', 2, 'DisplayName', 'Fitted Curve');    % Fitted curve
xlabel('data length [-]');
ylabel('steps count [-]');
legend('Location', 'best');
title('Insertion sort steps based on data length');





