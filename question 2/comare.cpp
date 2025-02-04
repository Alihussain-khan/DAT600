#include <iostream>
#include <vector>
#include <chrono>

void merge(std::vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    std::vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void merge_sort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        merge_sort(arr, left, mid);
        merge_sort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

double test_merge_sort(int input_size) {
    std::vector<int> arr(input_size);
    for (int i = 0; i < input_size; i++) {
        arr[i] = input_size - i;  // Reverse sorted array
    }

    auto start_time = std::chrono::high_resolution_clock::now();
    merge_sort(arr, 0, arr.size() - 1);
    auto end_time = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> elapsed = end_time - start_time;
    return elapsed.count();
}

int main() {
    std::vector<int> input_sizes = {1000, 10000, 100000, 1000000};
    for (int size : input_sizes) {
        double execution_time = test_merge_sort(size);
        std::cout << "C++ - Input size: " << size << ", Execution time: " << execution_time << " seconds\n";
    }
    return 0;
}