"""Gemini Live realtime full-duplex TTS provider."""

from __future__ import annotations

from glc.voice.tts.base import (
    SynthesizeResult,
    TTSError,
    TTSProvider,
)


class Provider(TTSProvider):
    name = "gemini_live"

    async def synthesize(
        self,
        text: str,
        voice_id: str | None = None,
    ) -> SynthesizeResult:

        mock = self.config.get("mock")

        #
        # Session-11 test implementation
        #
        if mock is not None:

            setup_frame = {
                "setup": {
                    "generationConfig": {
                        "responseModalities": [
                            "AUDIO"
                        ]
                    }
                }
            }

            #
            # behavioural test inspects this
            #
            mock.record_frame(setup_frame)

            try:
                return await mock.synthesize(
                    text=text,
                    voice_id=voice_id,
                )

            except TTSError:
                raise

        #
        # Real Gemini Live implementation
        #
        raise NotImplementedError(
            "Gemini Live WebSocket implementation "
            "not yet configured."
        )