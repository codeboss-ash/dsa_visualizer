# dsa_visualizer/app.py
import streamlit as st
import time
from algorithms import searching, sorting, tree_traversal, list_operations, stack_operations, queue_operations
from visualizations import search_visualizer, sort_visualizer, tree_visualizer, list_visualizer, stack_visualizer, queue_visualizer
from utility import generate_random_array, generate_bst_nodes

st.set_page_config(page_title="DSA Visualizer", layout="wide")

st.title("Interactive DSA & Data Structures Visualizer")

algorithm_type = st.sidebar.selectbox(
    "Select Operation Type",
    ["Searching", "Sorting", "Tree Traversal", "List Operations", "Stack Operations", "Queue Operations"]
)

if algorithm_type == "Searching":
    st.sidebar.subheader("Searching Algorithm Options")
    search_algo = st.sidebar.selectbox(
        "Select Search Algorithm",
        ["Linear Search", "Binary Search", "Jump Search"]
    )
    data_input = st.sidebar.text_area("Enter comma-separated numbers for the array:", "10,5,8,2,7,1,9,4,6,3", height=50)
    try:
        data_array = [int(x.strip()) for x in data_input.split(',')]
    except ValueError:
        st.sidebar.error("Invalid input. Please enter comma-separated numbers.")
        st.stop()
    target = st.sidebar.number_input("Target Value", value=5)

    st.subheader("Array")
    st.write(data_array)

    if st.button("Start Search"):
        placeholder = st.empty()

        def update_search_visualization(arr, highlighted, found):
            with placeholder.container():
                search_visualizer.visualize_search(arr, highlighted, found)

        if search_algo == "Linear Search":
            result_index, time_complexity, space_complexity = searching.linear_search(list(data_array), target, update_search_visualization)
        elif search_algo == "Binary Search":
            sorted_array = sorted(data_array)
            st.subheader("Sorted Array (for Binary Search)")
            st.write(sorted_array)
            result_index, time_complexity, space_complexity = searching.binary_search(list(sorted_array), target, update_search_visualization)
        elif search_algo == "Jump Search":
            sorted_array = sorted(data_array)
            st.subheader("Sorted Array (for Jump Search)")
            st.write(sorted_array)
            result_index, time_complexity, space_complexity = searching.jump_search(list(sorted_array), target, update_search_visualization)

        if result_index != -1:
            st.success(f"Target found at index: {result_index}")
        else:
            st.error("Target not found.")
        st.info(f"Time Complexity: {time_complexity}, Space Complexity: {space_complexity}")
        st.subheader("Explanation:")
        if search_algo == "Linear Search":
            st.write("Linear search iterates through each element of the array until the target is found or the end is reached.")
        elif search_algo == "Binary Search":
            st.write("Binary search works on sorted arrays. It repeatedly divides the search interval in half.")
        elif search_algo == "Jump Search":
            st.write("Jump search works on sorted arrays by jumping ahead by a fixed step and then performing a linear search.")

elif algorithm_type == "Sorting":
    st.sidebar.subheader("Sorting Algorithm Options")
    sort_algo = st.sidebar.selectbox(
        "Select Sorting Algorithm",
        ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Quick Sort"]
    )
    data_input = st.sidebar.text_area("Enter comma-separated numbers for the array:", "5,1,4,2,8", height=50)
    try:
        data_array = [int(x.strip()) for x in data_input.split(',')]
    except ValueError:
        st.sidebar.error("Invalid input. Please enter comma-separated numbers.")
        st.stop()

    st.subheader("Unsorted Array")
    st.write(data_array)

    if st.button("Start Sort"):
        placeholder = st.empty()

        def update_sort_visualization(arr, highlighted, swapped):
            with placeholder.container():
                sort_visualizer.visualize_sort(arr, highlighted, swapped)

        if sort_algo == "Bubble Sort":
            time_complexity, space_complexity = sorting.bubble_sort(list(data_array), update_sort_visualization)
        elif sort_algo == "Insertion Sort":
            time_complexity, space_complexity = sorting.insertion_sort(list(data_array), update_sort_visualization)
        elif sort_algo == "Selection Sort":
            time_complexity, space_complexity = sorting.selection_sort(list(data_array), update_sort_visualization)
        elif sort_algo == "Merge Sort":
            time_complexity, space_complexity = sorting.merge_sort(list(data_array), update_sort_visualization)
        elif sort_algo == "Quick Sort":
            time_complexity, space_complexity = sorting.quick_sort(list(data_array), update_sort_visualization)

        st.success("Array Sorted!")
        st.info(f"Time Complexity: {time_complexity}, Space Complexity: {space_complexity}")
        st.subheader("Explanation:")
        if sort_algo == "Bubble Sort":
            st.write("Bubble sort repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.")
        elif sort_algo == "Insertion Sort":
            st.write("Insertion sort builds the final sorted array one item at a time.")
        elif sort_algo == "Selection Sort":
            st.write("Selection sort repeatedly finds the minimum element from the unsorted part and puts it at the beginning.")
        elif sort_algo == "Merge Sort":
            st.write("Merge sort is a divide-and-conquer algorithm that divides the array into halves, recursively sorts them, and then merges the sorted halves.")
        elif sort_algo == "Quick Sort":
            st.write("Quick sort is also a divide-and-conquer algorithm that picks an element as pivot and partitions the array around the pivot.")

elif algorithm_type == "Tree Traversal":
    st.sidebar.subheader("Tree Traversal Options")
    traversal_algo = st.sidebar.selectbox(
        "Select Traversal Algorithm",
        ["Inorder", "Preorder", "Postorder", "Level Order"]
    )
    tree_input = st.sidebar.text_area("Enter comma-separated numbers for BST nodes:", "8,3,10,1,6,14,4,7,13", height=50)
    try:
        bst_nodes = [int(x.strip()) for x in tree_input.split(',')]
        root = tree_traversal.build_bst(bst_nodes)
    except ValueError:
        st.sidebar.error("Invalid input. Please enter comma-separated numbers.")
        st.stop()

    st.subheader("Binary Search Tree")
    tree_visualizer.visualize_tree(root)
    st.write("Tree Nodes:", sorted(bst_nodes))

    if st.button("Start Traversal"):
        placeholder = st.empty()

        def update_traversal_visualization(current_node, visited, time_complexity=None, space_complexity=None):
            with placeholder.container():
                tree_visualizer.visualize_tree(root, highlighted_nodes=[current_node])
                st.write("Traversal Order:", visited)
                if time_complexity and space_complexity:
                    st.info(f"Time Complexity: {time_complexity}, Space Complexity: {space_complexity}")
                time.sleep(0.5)

        if traversal_algo == "Inorder":
            tree_traversal.inorder_traversal(root, update_traversal_visualization)
        elif traversal_algo == "Preorder":
            tree_traversal.preorder_traversal(root, update_traversal_visualization)
        elif traversal_algo == "Postorder":
            tree_traversal.postorder_traversal(root, update_traversal_visualization)
        elif traversal_algo == "Level Order":
            time_complexity, space_complexity = tree_traversal.level_order_traversal(root, update_traversal_visualization)
            st.info(f"Time Complexity: {time_complexity}, Space Complexity: {space_complexity}")

        st.success("Traversal Complete!")
        st.subheader("Explanation:")
        if traversal_algo == "Inorder":
            st.write("Inorder traversal visits the left subtree, then the root, then the right subtree.")
        elif traversal_algo == "Preorder":
            st.write("Preorder traversal visits the root, then the left subtree, then the right subtree.")
        elif traversal_algo == "Postorder":
            st.write("Postorder traversal visits the left subtree, then the right subtree, then the root.")
        elif traversal_algo == "Level Order":
            st.write("Level order traversal visits nodes level by level, from left to right.")

elif algorithm_type == "List Operations":
    st.subheader("Linked List Operations")
    list_operations_type = st.selectbox(
        "Select Operation",
        ["Insert at Beginning", "Insert at End", "Insert at Position",
         "Delete at Beginning", "Delete at End", "Delete at Position"]
    )
    list_input = st.text_area("Enter comma-separated numbers for the linked list:", "1,2,3,4,5", height=50)
    try:
        list_data_initial = [int(x.strip()) for x in list_input.split(',')]
        head = list_operations.create_linked_list(list_data_initial)
    except ValueError:
        st.error("Invalid input. Please enter comma-separated numbers.")
        st.stop()

    st.subheader("Linked List")
    current_list_data, _, _ = list_operations.visualize_linked_list(head)
    st.write(" -> ".join(map(str, current_list_data)) if current_list_data else "Empty List")

    if list_operations_type == "Insert at Beginning":
        value_to_insert = st.number_input("Value to insert at the beginning:", value=0)
        if st.button("Insert"):
            head, time_complexity, space_complexity = list_operations.insert_at_beginning(head, value_to_insert)
            current_list_data, _, _ = list_operations.visualize_linked_list(head)
            st.subheader("Updated Linked List")
            st.write(" -> ".join(map(str, current_list_data)) if current_list_data else "Empty List")
            st.info(f"Time Complexity: {time_complexity}, Space Complexity: {space_complexity}")
            st.subheader("Explanation:")
            st.write("Inserting at the beginning of a linked list involves creating a new node and making it the new head.")
    elif list_operations_type == "Insert at End":
        value_to_insert = st.number_input("Value to insert at the end:", value=6)
        if st.button("Insert"):
            head, time_complexity, space_complexity = list_operations.insert_at_end(head, value_to_insert)
            current_list_data, _, _ = list_operations.visualize_linked_list(head)
            st.subheader("Updated Linked List")
            st.write(" -> ".join(map(str, current_list_data)) if current_list_data else "Empty List")
            st.info(f"Time Complexity: {time_complexity}, Space Complexity: {space_complexity}")
            st.subheader("Explanation:")
            st.write("Inserting at the end requires traversing to the last node and appending the new node.")
    elif list_operations_type == "Insert at Position":
        value_to_insert = st.number_input("Value to insert:", value=7)
        position_to_insert = st.number_input("Position to insert at (0-indexed):", value=2, min_value=0)
        placeholder = st.empty()
        if st.button("Insert"):
            def update_list_visualization(data_tuple):
                with placeholder.container():
                    list_visualizer.visualize_list(data_tuple[0], data_tuple[1], data_tuple[2])
                    time.sleep(0.5)
            result = list_operations.insert_at_position(head, value_to_insert, position_to_insert, update_list_visualization)
            if isinstance(result, tuple) and len(result) >= 3:
                head, time_complexity, space_complexity = result[:3]
                message = result[3] if len(result) > 3 else None
            else:
                head = result
                time_complexity, space_complexity = "O(n)", "O(1)"
                message = None
            current_list_data, _, _ = list_operations.visualize_linked_list(head)
            st.subheader("Updated Linked List")
            st.write(" -> ".join(map(str, current_list_data)) if current_list_data else "Empty List")
            st.info(f"Time Complexity: {time_complexity}, Space Complexity: {space_complexity}")
            if message:
                st.warning(message)
            st.subheader("Explanation:")
            st.write("Inserting at a specific position involves traversing to that position and linking the new node.")
    elif list_operations_type == "Delete at Beginning":
        if st.button("Delete"):
            head, time_complexity, space_complexity = list_operations.delete_at_beginning(head)
            current_list_data, _, _ = list_operations.visualize_linked_list(head)
            st.subheader("Updated Linked List")
            st.write(" -> ".join(map(str, current_list_data)) if current_list_data else "Empty List")
            st.info(f"Time Complexity: {time_complexity}, Space Complexity: {space_complexity}")
            st.subheader("Explanation:")
            st.write("Deleting at the beginning involves updating the head to the next node.")
    elif list_operations_type == "Delete at End":
        if st.button("Delete"):
            head, time_complexity, space_complexity = list_operations.delete_at_end(head)
            current_list_data, _, _ = list_operations.visualize_linked_list(head)
            st.subheader("Updated Linked List")
            st.write(" -> ".join(map(str, current_list_data)) if current_list_data else "Empty List")
            st.info(f"Time Complexity: {time_complexity}, Space Complexity: {space_complexity}")
            st.subheader("Explanation:")
            st.write("Deleting at the end requires traversing to the second-to-last node and removing the last node.")
    elif list_operations_type == "Delete at Position":
        position_to_delete = st.number_input("Position to delete at (0-indexed):", value=1, min_value=0)
        placeholder = st.empty()
        if st.button("Delete"):
            def update_list_visualization(data_tuple):
                with placeholder.container():
                    list_visualizer.visualize_list(data_tuple[0], data_tuple[1], data_tuple[2])
                    time.sleep(0.5)
            result = list_operations.delete_at_position(head, position_to_delete, update_list_visualization)
            if isinstance(result, tuple) and len(result) >= 3:
                head, time_complexity, space_complexity = result[:3]
                message = result[3] if len(result) > 3 else None
            else:
                head = result
                time_complexity, space_complexity = "O(n)", "O(1)"
                message = None
            current_list_data, _, _ = list_operations.visualize_linked_list(head)
            st.subheader("Updated Linked List")
            st.write(" -> ".join(map(str, current_list_data)) if current_list_data else "Empty List")
            st.info(f"Time Complexity: {time_complexity}, Space Complexity: {space_complexity}")
            if message:
                st.warning(message)
            st.subheader("Explanation:")
            st.write("Deleting at a specific position involves traversing to that position and updating the links to bypass the node to be deleted.")

elif algorithm_type == "Stack Operations":
    st.subheader("Stack Operations")
    operation_type = st.selectbox("Select Operation", ["Push", "Pop", "Peek", "Is Empty", "Size"])
    if 'stack_data' not in st.session_state:
        st.session_state['stack_data'] = []

    if operation_type == "Push":
        value_to_push = st.number_input("Value to push:", value=1)
        if st.button("Push"):
            st.session_state['stack_data'], time_complexity, space_complexity = stack_operations.Stack().push(st.session_state['stack_data'], value_to_push)
            stack_visualizer.display_stack_operation("Push", st.session_state['stack_data'], value_to_push, time_complexity, space_complexity)
            st.subheader("Explanation:")
            st.write("Push adds an element to the top of the stack.")
    elif operation_type == "Pop":
        if st.button("Pop"):
            current_stack = stack_operations.Stack()
            current_stack.items = list(st.session_state['stack_data'])
            popped_list, popped_item, time_complexity, space_complexity = current_stack.pop()
            st.session_state['stack_data'] = popped_list
            stack_visualizer.display_stack_operation("Pop", st.session_state['stack_data'], popped_item, time_complexity, space_complexity)
            st.subheader("Explanation:")
            st.write("Pop removes and returns the element at the top of the stack.")
    elif operation_type == "Peek":
        if st.session_state['stack_data']:
            peeked_item, time_complexity, space_complexity = stack_operations.Stack().peek(st.session_state['stack_data'])
            stack_visualizer.display_stack_operation("Peek", st.session_state['stack_data'], peeked_item, time_complexity, space_complexity)
            st.subheader("Explanation:")
            st.write("Peek returns the element at the top of the stack without removing it.")
        else:
            stack_visualizer.display_stack_operation("Peek", [], None, "O(1)", "O(1)")
            st.info("Stack is empty.")
    elif operation_type == "Is Empty":
        is_empty, time_complexity, space_complexity = stack_operations.Stack().is_empty(st.session_state['stack_data']), "O(1)", "O(1)"
        stack_visualizer.display_stack_operation("Is Empty", st.session_state['stack_data'], is_empty, time_complexity, space_complexity)
        st.subheader("Explanation:")
        st.write("Is Empty checks if the stack contains any elements.")
    elif operation_type == "Size":
        size, time_complexity, space_complexity = stack_operations.Stack().size(st.session_state['stack_data']), "O(1)", "O(1)"
        stack_visualizer.display_stack_operation("Size", st.session_state['stack_data'], size, time_complexity, space_complexity)
        st.subheader("Explanation:")
        st.write("Size returns the number of elements in the stack.")

elif algorithm_type == "Queue Operations":
    st.subheader("Queue Operations")
    operation_type = st.selectbox("Select Operation", ["Enqueue", "Dequeue", "Peek", "Is Empty", "Size"])
    if 'queue_data' not in st.session_state:
        st.session_state['queue_data'] = []

    if operation_type == "Enqueue":
        value_to_enqueue = st.number_input("Value to enqueue:", value=1)
        if st.button("Enqueue"):
            st.session_state['queue_data'], time_complexity, space_complexity = queue_operations.Queue().enqueue(st.session_state['queue_data'], value_to_enqueue)
            queue_visualizer.display_queue_operation("Enqueue", st.session_state['queue_data'], value_to_enqueue, time_complexity, space_complexity)
            st.subheader("Explanation:")
            st.write("Enqueue adds an element to the rear of the queue.")
    elif operation_type == "Dequeue":
        if st.button("Dequeue"):
            current_queue = queue_operations.Queue()
            current_queue.items = list(st.session_state['queue_data'])
            dequeued_list, dequeued_item, time_complexity, space_complexity = current_queue.dequeue()
            st.session_state['queue_data'] = dequeued_list
            queue_visualizer.display_queue_operation("Dequeue", st.session_state['queue_data'], dequeued_item, time_complexity, space_complexity)
            st.subheader("Explanation:")
            st.write("Dequeue removes and returns the element at the front of the queue.")
    elif operation_type == "Peek":
        if st.session_state['queue_data']:
            peeked_item, time_complexity, space_complexity = queue_operations.Queue().peek(st.session_state['queue_data'])
            queue_visualizer.display_queue_operation("Peek", st.session_state['queue_data'], peeked_item, time_complexity, space_complexity)
            st.subheader("Explanation:")
            st.write("Peek returns the element at the front of the queue without removing it.")
        else:
            queue_visualizer.display_queue_operation("Peek", [], None, "O(1)", "O(1)")
            st.info("Queue is empty.")
    elif operation_type == "Is Empty":
        is_empty, time_complexity, space_complexity = queue_operations.Queue().is_empty(st.session_state['queue_data']), "O(1)", "O(1)"
        queue_visualizer.display_queue_operation("Is Empty", st.session_state['queue_data'], is_empty, time_complexity, space_complexity)
        st.subheader("Explanation:")
        st.write("Is Empty checks if the queue contains any elements.")
    elif operation_type == "Size":
        size, time_complexity, space_complexity = queue_operations.Queue().size(st.session_state['queue_data']), "O(1)", "O(1)"
        queue_visualizer.display_queue_operation("Size", st.session_state['queue_data'], size, time_complexity, space_complexity)
        st.subheader("Explanation:")
        st.write("Size returns the number of elements in the queue.")