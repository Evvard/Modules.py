

Include a Makefile in your project to automate common tasks. It must contain the
following rules (mandatory lint implies the specified flags; it is strongly recommended to
try –strict for enhanced checking):
• install: Install project dependencies using pip, uv, pipx, or any other package
manager of your choice.
• run: Execute the main script of your project (e.g., via Python interpreter).
• debug: Run the main script in debug mode using Python’s built-in debugger (e.g.,
pdb).
• clean: Remove temporary files or caches (e.g., __pycache__, .mypy_cache) to
keep the project environment clean.






 lint: Execute the commands flake8 . and mypy . --warn-return-any
--warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs
--check-untyped-defs
• lint-strict (optional): Execute the commands flake8 . and mypy . --stricty



NAME	= push_swap
PYTHON	= python3

INSTALL	= installer les dependencies.txt avc pipe

RUN		= python3 a_maze_ing.py config.txt
DEBUG	= Run the main script in debug mode using Python’s built-in debugger (e.g., pdb).

CLEAN	= remove __pycache__, .mypy_cache

LINT	= flake8 . and mypy . --warn-return-any
			--warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs
			--check-untyped-defs

LINT-STRICT = flake8 . and mypy . --strict







all: $(NAME)

$(NAME): $(OBJ) $(LIBFT)
	$(CC) $(OBJ) $(LIBFT) -lm -o $(NAME)


clean:
	$(MAKE) clean -C $(LIBFT_DIR)
	$(RM) $(OBJ) $(OBJ_BONUS)

fclean: clean
	$(MAKE) fclean -C $(LIBFT_DIR)
	$(RM) $(NAME) $(NAME_BONUS)
	$(RM) -r $(OBJ_DIR)

re: fclean all

.PHONY: install run debug clean lint lint-strict


