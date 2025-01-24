# Changelog

## 0.2.0 (2025-01-24)

Full Changelog: [v0.1.2...v0.2.0](https://github.com/docugami/docugami-python/compare/v0.1.2...v0.2.0)

### Features

* **api:** api update ([#10](https://github.com/docugami/docugami-python/issues/10)) ([248bc86](https://github.com/docugami/docugami-python/commit/248bc863cfd8f54535e417aa8c2e0b7e2bfe8ea7))
* **api:** OpenAPI spec update ([#1](https://github.com/docugami/docugami-python/issues/1)) ([de8ca6c](https://github.com/docugami/docugami-python/commit/de8ca6cbc9f994feb692be829889a3b098d1dbcf))
* **api:** OpenAPI spec update ([#7](https://github.com/docugami/docugami-python/issues/7)) ([bd65cf2](https://github.com/docugami/docugami-python/commit/bd65cf21abfc88bd2f1372a9cb3aec62ca1ce1b7))
* **api:** OpenAPI spec update ([#8](https://github.com/docugami/docugami-python/issues/8)) ([d4a9bbf](https://github.com/docugami/docugami-python/commit/d4a9bbf036f88e2668bfa70cf39bb63ad880895a))
* generate initial Docugami python SDK ([b13d695](https://github.com/docugami/docugami-python/commit/b13d6950fd8b6986aaeb013d1d457081215f70fe))
* re-add upload libs ([3a7460c](https://github.com/docugami/docugami-python/commit/3a7460c3ebc9d4706ce6673fcbb22cdaec559079))


### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#24](https://github.com/docugami/docugami-python/issues/24)) ([1ee8e88](https://github.com/docugami/docugami-python/commit/1ee8e880dee059fe1bde36d81d2db8480b881c94))
* **client:** only call .close() when needed ([#38](https://github.com/docugami/docugami-python/issues/38)) ([fe8a47a](https://github.com/docugami/docugami-python/commit/fe8a47a35bf71100f7e1a3b7c78c607ff32d255d))
* correctly handle deserialising `cls` fields ([#41](https://github.com/docugami/docugami-python/issues/41)) ([f18f0d6](https://github.com/docugami/docugami-python/commit/f18f0d60cb6b2c8d92692713d447f1d02fbf61f0))
* **tests:** make test_get_platform less flaky ([#44](https://github.com/docugami/docugami-python/issues/44)) ([6adeacf](https://github.com/docugami/docugami-python/commit/6adeacf136650ea5841a740a5d847e3684b2522d))


### Chores

* add missing isclass check ([#36](https://github.com/docugami/docugami-python/issues/36)) ([226eeff](https://github.com/docugami/docugami-python/commit/226eeff8d1612152ef1b28b8b1def73bc551342c))
* go live ([#9](https://github.com/docugami/docugami-python/issues/9)) ([e439394](https://github.com/docugami/docugami-python/commit/e43939426a2878f74aa2dda5830b251bdf6dbd48))
* **internal:** avoid pytest-asyncio deprecation warning ([#45](https://github.com/docugami/docugami-python/issues/45)) ([85d1493](https://github.com/docugami/docugami-python/commit/85d1493922c3c35ec8429f5d6c803f9ad17d27a7))
* **internal:** bump httpx dependency ([#37](https://github.com/docugami/docugami-python/issues/37)) ([caa2575](https://github.com/docugami/docugami-python/commit/caa2575db384d3906213d2f0d125afc5b0d6b3f8))
* **internal:** bump pydantic dependency ([#27](https://github.com/docugami/docugami-python/issues/27)) ([2586ff7](https://github.com/docugami/docugami-python/commit/2586ff758729cba2d57dafd0d9d1f423818bf80b))
* **internal:** bump pyright ([#25](https://github.com/docugami/docugami-python/issues/25)) ([8870f73](https://github.com/docugami/docugami-python/commit/8870f739cee58fb6cf53989860e424ef306e4155))
* **internal:** bump pyright ([#29](https://github.com/docugami/docugami-python/issues/29)) ([b0978a0](https://github.com/docugami/docugami-python/commit/b0978a00edacd28b9ec1ae6a530ecd1259917568))
* **internal:** codegen related update ([#30](https://github.com/docugami/docugami-python/issues/30)) ([dedf379](https://github.com/docugami/docugami-python/commit/dedf379769f9e22dbd6de1b571b0ef95e3b7aecc))
* **internal:** codegen related update ([#31](https://github.com/docugami/docugami-python/issues/31)) ([a99ab7e](https://github.com/docugami/docugami-python/commit/a99ab7e316c6dafe42b82fef2f5daf952feae72f))
* **internal:** codegen related update ([#32](https://github.com/docugami/docugami-python/issues/32)) ([59b0d64](https://github.com/docugami/docugami-python/commit/59b0d647b549a9d8f9a9ebd65fe78caa6e1033da))
* **internal:** codegen related update ([#33](https://github.com/docugami/docugami-python/issues/33)) ([8b26006](https://github.com/docugami/docugami-python/commit/8b2600696a876c4e4fe5c2fe0ea348fbf9058f32))
* **internal:** codegen related update ([#35](https://github.com/docugami/docugami-python/issues/35)) ([5d8a1b2](https://github.com/docugami/docugami-python/commit/5d8a1b268f04619bdb3637ff9565f34e2fd64532))
* **internal:** codegen related update ([#40](https://github.com/docugami/docugami-python/issues/40)) ([c5a91b8](https://github.com/docugami/docugami-python/commit/c5a91b8ebe0dc005665bedd38ce347311be04158))
* **internal:** codegen related update ([#42](https://github.com/docugami/docugami-python/issues/42)) ([3ac468a](https://github.com/docugami/docugami-python/commit/3ac468ab1d76101fc54702a7a0ab37def0d6887a))
* **internal:** exclude mypy from running on tests ([#23](https://github.com/docugami/docugami-python/issues/23)) ([849fd5b](https://github.com/docugami/docugami-python/commit/849fd5b2fd1e3563413e514e2273e0d08d056528))
* **internal:** fix compat model_dump method when warnings are passed ([#20](https://github.com/docugami/docugami-python/issues/20)) ([22bc38d](https://github.com/docugami/docugami-python/commit/22bc38d6cc1bf357094187d7411bdf1923013d40))
* **internal:** fix some typos ([#34](https://github.com/docugami/docugami-python/issues/34)) ([fe7d98e](https://github.com/docugami/docugami-python/commit/fe7d98e063bfb8b8c3b5cb8620a199b1d566a0a8))
* **internal:** minor formatting changes ([#47](https://github.com/docugami/docugami-python/issues/47)) ([a587854](https://github.com/docugami/docugami-python/commit/a587854e142b2b5a70c60a0b1ffe1923a65413be))
* **internal:** minor style changes ([#46](https://github.com/docugami/docugami-python/issues/46)) ([6ac9cc5](https://github.com/docugami/docugami-python/commit/6ac9cc5c203d6471b831f3b3b256df09f37ca9c4))
* make the `Omit` type public ([#26](https://github.com/docugami/docugami-python/issues/26)) ([4660af2](https://github.com/docugami/docugami-python/commit/4660af231f2f109f0888709756159f67082ef051))
* rebuild project due to codegen change ([#11](https://github.com/docugami/docugami-python/issues/11)) ([309e375](https://github.com/docugami/docugami-python/commit/309e375da85d576b114579000e180762e6d71d6c))
* rebuild project due to codegen change ([#12](https://github.com/docugami/docugami-python/issues/12)) ([477698d](https://github.com/docugami/docugami-python/commit/477698df5ea0a2bc9395e243a98415d4326def46))
* rebuild project due to codegen change ([#13](https://github.com/docugami/docugami-python/issues/13)) ([e286946](https://github.com/docugami/docugami-python/commit/e28694643756532da7999ab96d0b0db5d5bcf8a7))
* rebuild project due to codegen change ([#15](https://github.com/docugami/docugami-python/issues/15)) ([2328605](https://github.com/docugami/docugami-python/commit/2328605cf66d05fe260b2760445d6eda0dc2f2d9))
* rebuild project due to codegen change ([#16](https://github.com/docugami/docugami-python/issues/16)) ([6562aea](https://github.com/docugami/docugami-python/commit/6562aea488adcaea62db180b254bb401601a27b6))
* rebuild project due to codegen change ([#17](https://github.com/docugami/docugami-python/issues/17)) ([2203be8](https://github.com/docugami/docugami-python/commit/2203be8785cc805ea12b9da618d889c2fd690815))
* rebuild project due to codegen change ([#18](https://github.com/docugami/docugami-python/issues/18)) ([65f7394](https://github.com/docugami/docugami-python/commit/65f7394d9678d9a827aa8fe1082ccff08218a846))
* rebuild project due to codegen change ([#19](https://github.com/docugami/docugami-python/issues/19)) ([b2cab04](https://github.com/docugami/docugami-python/commit/b2cab0435b871d86caf595cc512e480863ad6433))
* remove now unused `cached-property` dep ([#22](https://github.com/docugami/docugami-python/issues/22)) ([64baa24](https://github.com/docugami/docugami-python/commit/64baa24b75f1d67e784d0a1ab1cc17540516c2ae))


### Documentation

* add info log level to readme ([#21](https://github.com/docugami/docugami-python/issues/21)) ([3351582](https://github.com/docugami/docugami-python/commit/33515825af4e93fe091a5e8fc8c5665890ad5775))
* fix typos ([#39](https://github.com/docugami/docugami-python/issues/39)) ([502e5c2](https://github.com/docugami/docugami-python/commit/502e5c2b965acd74488a18dbbc05af3f9c8edbfe))
* **raw responses:** fix duplicate `the` ([#43](https://github.com/docugami/docugami-python/issues/43)) ([7a26253](https://github.com/docugami/docugami-python/commit/7a262537463d16853844f2a474edbd938ca7b29c))
* **readme:** fix http client proxies example ([#28](https://github.com/docugami/docugami-python/issues/28)) ([28ca372](https://github.com/docugami/docugami-python/commit/28ca3729c08a6a7ca985e6781953b9a32d7a2314))

## 0.1.0 (2023-12-08)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/docugami/docugami-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** OpenAPI spec update ([#1](https://github.com/docugami/docugami-python/issues/1)) ([c3cda6f](https://github.com/docugami/docugami-python/commit/c3cda6f757128f9ee4862b90205d7de36e3f2d31))
* generate initial Docugami python SDK ([b13d695](https://github.com/docugami/docugami-python/commit/b13d6950fd8b6986aaeb013d1d457081215f70fe))
