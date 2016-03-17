x, y, z, n = int(raw_input()), int(raw_input()), int(raw_input()), int(raw_input())
print [[xi,yi,zi] for xi in range(x+1) for yi in range(y+1) for zi in range(z+1) if (xi+yi+zi) is not n]