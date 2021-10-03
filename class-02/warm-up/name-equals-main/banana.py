module_name = "banana"

print(
    f"I am {module_name} module with __name__ of {__name__}. I run once when loaded"
)

if __name__ == "__main__":
    print(
        f"I am {module_name} module with __name__ of {__name__} and only run when executed as a 'script'"
    )
else:
    print(
        f"I am {module_name} module with __name__ of {__name__} and only run when imported"
    )
