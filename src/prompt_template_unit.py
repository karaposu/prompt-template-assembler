
class PromptTemplateUnit:
    def __init__(self, name, statement_suffix=None, placeholder_proclamation=None, placeholder=None, info=None, category=None):
        self.name = name
        self.statement_suffix = statement_suffix
        self.placeholder_proclamation = placeholder_proclamation
        self.placeholder = placeholder
        self.info = info
        self.category = category
        self.marked_as_question=False
        self.answered = False
        self.question_suffix = "What is "



    # def answered(self):
    #     self.marked_as_question = False
    #     self.answered = True

    def make_question(self):
        self.marked_as_question = True

    def close_question(self, answered=True):
        self.marked_as_question = False
        self.answered = answered



        # self.answered = True

    def format_info(self,info):

        if info:
            return f"{info}\n"
        return ""

    def format_placeholder(self, placeholder, pretty):

        if pretty and placeholder:
            return f":\n{{{placeholder}}}\n\n-------------"
        elif placeholder:
            return f": {{{placeholder}}}\n\n-------------"
        return ""

    def format_suffix(self, suffix, markdown_formatting):

        if markdown_formatting and suffix:
            return f"### {suffix}"
        return suffix if suffix else ""

    def construct_statement(self, pretty=True, markdown_formatting=True):

        if self.marked_as_question:
            statement = self.format_info(self.info)
            question_suffix = self.format_suffix(self.question_suffix, markdown_formatting)
            return f"{statement}{question_suffix} {self.placeholder_proclamation}?"

        # Handle declarative formatting
        statement = self.format_info(self.info)
        statement_suffix = self.format_suffix(self.statement_suffix, markdown_formatting)

        # Build the main body of the statement
        if statement_suffix:
            statement += f"{statement_suffix} {self.placeholder_proclamation}"

        # Format the placeholder
        statement += self.format_placeholder(self.placeholder, pretty)

        return statement

