def is_valid_post_format(posts):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in posts:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0   




def reverse_comments_queue(comments):
    stack = []

    for comment in comments:
        stack.append(comment)

    reversed_comments = []
    while stack:
        reversed_comments.append(stack.pop())

    return reversed_comments  



def is_symmetrical_title(title):
    cleaned = ""
    for char in title:
        if char.isalpha():
            cleaned += char.lower()

    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return  True



def engagement_boost(engagements):
    squared_engagements = []

    # Square every number, but remember its original index too,
    # since squaring can scramble the order (negatives become positive)
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))

    # Sort by the square value, largest first
    # (largest first makes it easier to fill 'result' from the back)
    squared_engagements.sort(reverse=True)

    result = [0] * len(engagements)  # pre-made list of the right size, filled with 0s
    position = len(engagements) - 1  # start filling from the LAST slot

    # Place each square into its correct sorted position, back to front
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1

    return result   



def engagement_boost(engagements):
    n = len(engagements)
    result = [0] * n

    left = 0
    right = n - 1
    position = n - 1  # fill the result array from the back (largest first)

    while left <= right:
        left_square = engagements[left] * engagements[left]
        right_square = engagements[right] * engagements[right]

        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1

        position -= 1

    return result