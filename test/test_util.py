# Copyright (C) 2020 Dmitry Marakasov <amdmi3@amdmi3.ru>
#
# This file is part of repology
#
# repology is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# repology is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with repology.  If not, see <http://www.gnu.org/licenses/>.

import unittest

from vulnupdater.util import escaped_split


class TestHostManager(unittest.TestCase):
    def test_escaped_split(self):
        self.assertEqual(escaped_split('1:2:3', ':'), ['1', '2', '3'])
        self.assertEqual(escaped_split('::', ':'), ['', '', ''])
        self.assertEqual(escaped_split('\\::', ':'), [':', ''])
        self.assertEqual(escaped_split('\\\\::', ':'), ['\\', '', ''])


if __name__ == '__main__':
    unittest.main()
