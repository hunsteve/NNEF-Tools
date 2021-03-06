# Copyright (c) 2017 The Khronos Group Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import _nnef


def parse_file(graph_fn, quant_fn=None, stdlib=None, lowered=[]):
    return _nnef.parse_file(graph_fn, quantization=quant_fn, stdlib=stdlib, lowered=lowered)


def parse_string(graph_str, quant_str=None, stdlib=None, lowered=[]):
    return _nnef.parse_string(graph_str, quantization=quant_str, stdlib=stdlib, lowered=lowered)
