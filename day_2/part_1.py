def surface_area(length, width, height):
    return 2 * length * width + 2 * width * height + 2 * height * length

def slack(length, width, height):
    return min([length * width, width * height, height * length])

def paper_needed(present_size):
    return surface_area(*present_size) + slack(*present_size)

total_paper = 0
with open('input.txt') as f:
    for line in f:
        present_size = [int(n) for n in line.strip().split('x')]
        total_paper += paper_needed(present_size)
print total_paper
