clear
close all

is_count = [1539   1829   2210   2627   3159   3740   4464   5355   6440   7749 9315  11174  13365  16109  19305  23219  27965  33669  40469  48827 58995  71252  85904 103739 125249];

ms_count = [430  475  531  591  661  731  811  901 1001 1111 1239 1382 1536 1712 1899 2108 2339 2595 2895 3231 3603 4011 4455 4947 5487];

hs_count = [347  383  436  475  531  594  658  731  824  923 1035 1140 1275 1421 1575 1769 1965 2185 2439 2717 3021 3384 3792 4189 4675];

qs_count = [1649   1949   2342   2771   3317   3912   4652   5561   6666   7997 9587  11472  13691  16467  19697  23649  28437  34187  41037  49451 59681  72006  86732 104649 126249];

init_datalen = 50;
scale_coef = 1.1;
datalens = zeros(1, length(is_count));
datalens(1) = init_datalen;
datalens(1) = floor(datalens(1)*scale_coef);

if (length(is_count) == length(ms_count)) && ...
   (length(ms_count) == length(hs_count)) && ...
   (length(hs_count) == length(qs_count))

    for i = 2:25
        datalens(i) = floor(datalens(i-1)*scale_coef);

    end
else
    error('Data does not have the same length')
end

%--------------------- Insertion sort -------------------------------------

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

% Plot the data points and the fitted curve
x_fit = linspace(min(datalens), max(datalens), 100);  % Generate smooth x values for plotting
y_fit = a * x_fit.^2 + b * x_fit + c;            % Compute the corresponding y values

plot(datalens, is_count, 'ro', 'MarkerSize', 8, 'DisplayName', 'Data Points'); % Original data points
plot(x_fit, y_fit, 'b-', 'LineWidth', 2, 'DisplayName', 'Fitted Curve');    % Fitted curve
xlabel('data length [-]');
ylabel('steps count [-]');
legend('Location', 'best');
title('Insertion sort steps based on data length');

%--------------------- Merge sort -----------------------------------------
ms_count = ms_count(:);

% Construct the design matrix for the a*n*log(n) + b*n + c function
% Each row is [x*log2(x), x, 1]
A = [datalens.*log2(datalens), datalens, ones(size(datalens))];

% Solve the equation A * coeffs = y to get the coefficients
coeffs = A \ ms_count;

% Extract coefficients a, b, c
a = coeffs(1);
b = coeffs(2);
c = coeffs(3);
fprintf('The quadratic function is: y = %.4fx^2 + %.4fx + %.4f\n', a, b, c);

figure(2)
hold on
grid on

% Plot the data points and the fitted curve
x_fit = linspace(min(datalens), max(datalens), 100);  % Generate smooth x values for plotting
y_fit = a * x_fit.*log2(x_fit) + b * x_fit + c;            % Compute the corresponding y values

plot(datalens, ms_count, 'ro', 'MarkerSize', 8, 'DisplayName', 'Data Points'); % Original data points
plot(x_fit, y_fit, 'b-', 'LineWidth', 2, 'DisplayName', 'Fitted Curve');    % Fitted curve
xlabel('data length [-]');
ylabel('steps count [-]');
legend('Location', 'best');
title('Merge sort steps based on data length');

%--------------------- Heap sort ------------------------------------------
hs_count = hs_count(:);

% Construct the design matrix for the a*n*log(n) + b*n + c function
% Each row is [x*log2(x), x, 1]
A = [datalens.*log2(datalens), datalens, ones(size(datalens))];

% Solve the equation A * coeffs = y to get the coefficients
coeffs = A \ hs_count;

% Extract coefficients a, b, c
a = coeffs(1);
b = coeffs(2);
c = coeffs(3);
fprintf('The quadratic function is: y = %.4fx^2 + %.4fx + %.4f\n', a, b, c);

figure(3)
hold on
grid on

% Plot the data points and the fitted curve
x_fit = linspace(min(datalens), max(datalens), 100);  % Generate smooth x values for plotting
y_fit = a * x_fit.*log2(x_fit) + b * x_fit + c;            % Compute the corresponding y values

plot(datalens, hs_count, 'ro', 'MarkerSize', 8, 'DisplayName', 'Data Points'); % Original data points
plot(x_fit, y_fit, 'b-', 'LineWidth', 2, 'DisplayName', 'Fitted Curve');    % Fitted curve
xlabel('data length [-]');
ylabel('steps count [-]');
legend('Location', 'best');
title('Heap sort steps based on data length');

%--------------------- Quick sort -----------------------------------------
qs_count = qs_count(:);

% Construct the design matrix for the quadratic function
% Each row is [x^2, x, 1]
A = [datalens.^2, datalens, ones(size(datalens))];

% Solve the equation A * coeffs = y to get the coefficients
coeffs = A \ qs_count;

% Extract coefficients a, b, c
a = coeffs(1);
b = coeffs(2);
c = coeffs(3);
fprintf('The quadratic function is: y = %.4fx^2 + %.4fx + %.4f\n', a, b, c);

figure(4)
hold on
grid on

% Plot the data points and the fitted curve
x_fit = linspace(min(datalens), max(datalens), 100);  % Generate smooth x values for plotting
y_fit = a * x_fit.^2 + b * x_fit + c;            % Compute the corresponding y values

plot(datalens, qs_count, 'ro', 'MarkerSize', 8, 'DisplayName', 'Data Points'); % Original data points
plot(x_fit, y_fit, 'b-', 'LineWidth', 2, 'DisplayName', 'Fitted Curve');    % Fitted curve
xlabel('data length [-]');
ylabel('steps count [-]');
legend('Location', 'best');
title('Quick sort steps based on data length');


% use in case of logaritmic axis
% set(gca, 'XScale', 'log')
% set(gca, 'YScale', 'log')
