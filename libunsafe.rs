#[no_mangle]
pub extern "C" fn quicksort(arr: *mut i32, len: usize) {
    let slice = unsafe { std::slice::from_raw_parts_mut(arr, len) };
    quicksort_recursive(slice);
}

fn quicksort_recursive<T: Ord>(arr: &mut [T]) {
    if arr.len() <= 1 {
        return;
    }
    let pivot_index = partition(arr);
    quicksort_recursive(&mut arr[0..pivot_index]);
    quicksort_recursive(&mut arr[pivot_index + 1..]);
}

fn partition<T: Ord>(arr: &mut [T]) -> usize {
    let pivot_index = arr.len() / 2;
    unsafe {
        // Swap the pivot with the last element
        arr.swap(pivot_index, arr.len() - 1);
    }

    let mut i = 0;

    // Loop through all elements except the pivot
    for j in 0..arr.len() - 1 {
        unsafe {
            // Use raw pointers to access elements directly
            if *arr.get_unchecked(j) <= *arr.get_unchecked(arr.len() - 1) {
                arr.swap(i, j);
                i += 1;
            }
        }
    }

    // Swap the pivot into its correct position
    unsafe {
        arr.swap(i, arr.len() - 1);
    }

    i
}
