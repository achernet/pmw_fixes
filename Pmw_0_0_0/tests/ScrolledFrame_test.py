import Test
import Pmw

Test.initialise()

c = Pmw.ScrolledFrame

def _createInterior():
    w = Test.currentWidget()
    for i in range(2):
	lb = Pmw.ScrolledListBox(w.interior(),
		items = range(20), listbox_height = 6)
	lb.pack(padx = 10, pady = 10)

kw_1 = {'labelpos': 'n', 'label_text': 'ScrolledFrame'}
tests_1 = (
  (c.pack, (), {'padx' : 10, 'pady' : 10, 'fill' : 'both', 'expand' : 1}),
  (Test.num_options, (), 11),
  (_createInterior, ()),
  ('hull_background', 'aliceblue'),
  ('Scrollbar_borderwidth', 3),
  ('hull_cursor', 'gumby'),
  ('label_text', 'Label'),
  ('Scrollbar_repeatdelay', 200),
  ('Scrollbar_repeatinterval', 105),
  ('vscrollmode', 'none'),
  ('vscrollmode', 'static'),
  ('vscrollmode', 'dynamic'),
  ('hscrollmode', 'none'),
  ('hscrollmode', 'static'),
  ('hscrollmode', 'dynamic'),
  ('Scrollbar_width', 20),
  ('vscrollmode', 'bogus', 'ValueError: bad vscrollmode ' +
    'option "bogus": should be static, dynamic, or none'),
  ('hscrollmode', 'bogus', 'ValueError: bad hscrollmode ' +
    'option "bogus": should be static, dynamic, or none'),
)

kw_2 = {
  'hscrollmode' : 'dynamic',
  'label_text' : 'Label',
  'labelpos' : 'n',
  'scrollmargin': 20,
}
tests_2 = (
  (c.pack, (), {'padx' : 10, 'pady' : 10, 'fill' : 'both', 'expand' : 1}),
)

alltests = (
  (tests_1, kw_1),
  (tests_2, kw_2),
)

testData = ((Pmw.ScrolledFrame, alltests),)

if __name__ == '__main__':
    Test.runTests(testData)