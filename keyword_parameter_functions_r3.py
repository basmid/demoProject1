# Example 3
import time
print("**** Start Example 3 *****")
def verify_process_is_complete(type_of_process, max_retry=10, time_to_sleep=2):

    print("Verifying the process '{}' is complete.".format(type_of_process))

    completed = False
    for i in range(1, max_retry):
        print("Attempt number: {}".format(i))

        # code
        if i == 6:
            completed = True

        if completed == True:
            print("The process is complete. Stopping rechecking.")
            break
        else:
            print("The process is not complete. Sleeping for {} seconds and retrying.".format(time_to_sleep))
            time.sleep(2)

    if not completed:
        raise Exception("The process is did not complete after waiting for '{}' seconds.".format(max_retry * time_to_sleep))

    else:
        return None

# verify_process_is_complete('bla')
verify_process_is_complete('bla',7,4)


