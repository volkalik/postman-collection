from Basic.ssr_file import SomeResourceClient


def test_ssr():
    some_resource_client = SomeResourceClient("https://qa-xgs.xenial.com")
    appversion = some_resource_client.get_appversion("inf")
    assert appversion
    assert isinstance(appversion, str)
    assert appversion == "BUILD-3.8.182"

