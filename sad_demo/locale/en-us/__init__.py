# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from mycroft.skills.core import intent_handler
from mycroft.skills import MycroftSkill


class WolframAlphaSkill(MycroftSkill):

    @intent_handler("sad.intent")
    def handle_sad(self, message):
        self.speak_dialog("sad_response")


def create_skill():
    return WolframAlphaSkill()
