print(f"I am apple module with __name__ of {__name__}. I run once when loaded")

print(f"I am apple module and am about to import banana")

import banana

print(f"I am apple module and I imported {banana.module_name}")

if __name__ == "__main__":
    print(
        f"I am apple module with __name__ of {__name__} and only run when executed as a 'script'"
    )
else:
    print(
        f"I am apple module with __name__ of {__name__} and only run when imported"
    )
