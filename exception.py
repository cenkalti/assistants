from akson import Assistant, Chat


class ExceptionRaiser(Assistant):

    async def run(self, chat: Chat) -> None:
        match message := chat.state.messages[-1].content.strip():
            case "zero":
                1 / 0  # type: ignore
            case "assert":
                assert False
            case _:
                raise Exception(message)


exception_raiser = ExceptionRaiser()
