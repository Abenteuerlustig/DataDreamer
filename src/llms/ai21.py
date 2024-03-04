from functools import cached_property

from ._litellm import LiteLLM


class AI21(LiteLLM):
    def __init__(
        self,
        model_name: str,
        api_key: None | str = None,
        retry_on_fail: bool = True,
        cache_folder_path: None | str = None,
        **kwargs,
    ):
        super().__init__(
            model_name=model_name,
            api_key=api_key,
            retry_on_fail=retry_on_fail,
            cache_folder_path=cache_folder_path,
            **kwargs,
        )
        self._model_name_prefix = ""

    @cached_property
    def model_card(self) -> None | str:
        return "https://www.ai21.com/blog/introducing-j2"

    @cached_property
    def license(self) -> None | str:
        return "https://www.ai21.com/terms-of-use"


__all__ = ["AI21"]
