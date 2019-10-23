from annotations import annotate
from annotations import annotations


def test_annotate():
    @annotate('my.test.annotation1')
    @annotate('my.test.annotation2')
    class TestClass1:
        pass

    @annotate('my.test.annotation2')
    @annotate('my.test.annotation3')
    class TestClass2:
        pass

    @annotate('my.test.annotation2')
    class TestClass3:
        pass

    assert annotations.get_annotations_of_class(TestClass1) == ('my.test.annotation2', 'my.test.annotation1')
    assert annotations.get_annotations_of_class(TestClass2) == ('my.test.annotation3', 'my.test.annotation2')
    assert annotations.get_annotations_of_class(TestClass3) == ('my.test.annotation2',)
    assert annotations.get_classes_by_annotation_name('my.test.annotation1') == [TestClass1]
    assert annotations.get_classes_by_annotation_name('my.test.annotation2') == [TestClass1, TestClass2, TestClass3]
    assert annotations.get_classes_by_annotation_name('my.test.annotation3') == [TestClass2]
