"""
    code interview solution for company Zalando, Berlin, Germany
    Date: 2019-11-22
    score is  88%, view Codility, result is here  https://app.codility.com/c/feedback/QPPYH5-2UV/ until 2019-12-22

    Summary:
        I was very concerned that it is not 100% result, tasks was similar to each other and not very hard at all,
        some how few tricky test cases failed that time.
        But even though I was invited to the next round - face to face technical interview - remote.

    Next Round Overview:
    I had pretty good interview, everything went smoothly tha time:
      - talk part (self introduction, current/past project experience, team, etc)
      - answered all technical questions
            (Java - new feature in 8 streams lambda, concurrency and thread, cons of lambda (you cant reuse it), etc.
             - went well enough even I was not read to speak about Java at all, some how I expected  Python question for
              this role, Python Software Engineer)
            (architecture and design - favorite disign patterns, tinny url architecture etc).
    Overall, I had very good felling, it was the first time when I was 99% sure I have passed it, but unfortunately
    got answer bellow, which was kind of frustrating for me. Bad luck ):

    Hi Volodymyr,
    Thank you for taking the time to speak to our team about the position of Senior Backend Engineer -
     Text Analytics/NLP! It was a pleasure to learn more about your skills and accomplishments.
    Unfortunately, after reviewing feedback from your interview, we regret to inform you that your application was not
     selected for further consideration for this position. Please understand that this decision does not reflect on your
     abilities, but rather on our current needs and requirements.
    As we continue to grow we may have opportunities in the near future that could be a match for you, so we encourage
    you to keep in touch via this link. You will be the first to receive relevant info on developments in e-commerce,
    open positions, meetups we host, and conferences we will attend.
    In the meantime, we would like to hear your feedback on your personal experience with our recruitment process. In a
     couple of days, we will invite you to take a short survey. Your input will help us offer a better candidate
     experience. Thank you once again for your interest in a career with Zalando SE. We wish you all the best with
      your professional endeavors.
    Sara Bettencourt
    Recruitment Specialist Technology
    Sourcing & Recruiting Team
    Zalando SE
"""


class Task1:
    """
        solution for Task1
    """
    @staticmethod
    def solution(given_ar):
        """
         solution itself
          write your code in Python 3.6
          O(2*N), => could be O(N) if step 2 logic put in step 1 as after-math after "if"

        :param given_ar: input data
        :return:
        """
        # TODO: I will optimize it next time
        result = 0
        dic_calc = {}

        # step 1 - find all pears loop
        for num_item in given_ar:
            if num_item in dic_calc:
                dic_calc[num_item] += 1
            else:
                dic_calc[num_item] = 1
            # here may be logic from step 2

        # step 2 - calculate all pears combination
        for val in dic_calc.values():
            if val > 1:
                n = val - 1
                result += n * (1 + n) // 2
        return result

    @classmethod
    def run_test(cls):
        """
        execute solution for given test cases
        :return: just print
        """
        # given data - test example
        # Case 1
        A = [0] * 6
        A[0] = 3
        A[1] = 5
        A[2] = 6
        A[3] = 3
        A[4] = 3
        A[5] = 5
        print(cls.solution(A))

        # Case 2
        A[0] = 3
        A[1] = 5
        A[2] = 6
        A[3] = 3
        A[4] = 3
        A[5] = 5

        print(cls.solution(A))


Task1.run_test()

"""
    Compilation successful.
    
    Example test:   [2, 1, 3, 5, 4]
    OK
    
    Example test:   [2, 3, 4, 1, 5]
    OK
    
    Example test:   [1, 3, 4, 2, 5]
    OK
    
    Your test case: [2, 1, 3, 5, 4]
    Returned value: 3
    
    Your code is syntactically correct and works properly on the example test.
    Note that the example tests are not part of your score. On submission at least 8 test cases not shown here will assess 
    your solution.
"""


class Task2:
    """
        solution for Task2
    """
    @staticmethod
    def solution(given_ar):
        """
        solution itself
         write your code in Python 3.6
        :param given_ar: input array
        :return:
        """
        moments = 0
        sum_bulb = 0
        index = 1

        # overflow sum_bulb and exp_sum wont happen, because
        # "if the operations are done in pure python, because python integers have arbitrary precision"
        for bulb in given_ar:
            sum_bulb += bulb
            exp_sum = index * (1 + index) / 2
            if sum_bulb == exp_sum:
                moments += 1
            index += 1

        return moments


class Task3:
    """
        solution for Task3
    """
    @staticmethod
    def solution(given_str):
        """
             solution itself
              write your code in Python 3.6
             :param given_str: input str
             :return:
             """
        result = 0
        lead_zero_index = 0

        # get rid of leading zero
        while given_str[lead_zero_index] == "0":
            lead_zero_index += 1

        # run calculation
        current_index = len(given_str)
        for last_bit in reversed(given_str):
            current_index -= 1
            # count until met leading zeros
            if current_index > lead_zero_index:
                if last_bit == "0":
                    result += 1
                else:
                    result += 2
            # last '1' should be count as last step
            elif current_index == lead_zero_index:
                result += 1

        return result

    @classmethod
    def run_test(cls):
        """
        execute solution for given test cases
        :return: just print
        """
        # 1 1100‬
        #   1110‬
        #    111
        #    110
        #     11
        #      10
        #      1
        #      0
        s = "011100"
        print(cls.solution(s))


Task3.run_test()
