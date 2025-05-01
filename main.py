def main():
    print("x = " + vertical_fraction("-b +/- sqrt(b^2 - 4ac)", "2a"))

#Make fractions look like real math equations    
def vertical_fraction(numerator, denominator):
    width = max(len(str(numerator)), len(str(denominator)))
    top = str(numerator).center(width)
    line = "-" * width
    bottom = str(denominator).center(width)
    return f"{top}\n{line}\n{bottom}"

main()
