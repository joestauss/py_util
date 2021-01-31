from cli_selector import cli_selector

if __name__ == '__main__':
    cli_selector( [
        'Single-choice selection mode.',
        'Why not try selecting a few to see how it handles invalid inputs?',
        'This is the third option.',
        'This is the fourth option.,',
        'This is the final option.'])
        
    cli_selector( [
        'multiple-choice selection mode.',
        'Why not try "mistyping" one to see how it handles invalid inputs?',
        'This is the third option.',
        'This is the fourth option.,',
        'This is the final option.'], mode='multiple')
