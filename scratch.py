import xml4h
from config_generator.override_xml_writer import override_write_node

from lxml import etree


def xml4h_test1():
    root = xml4h.build('root') \
            .e('level1') \
                .e('level2').t('text') \
                .up() \
                .e('level2').t('">="') \
                .up() \
            .up()
        # .up()
    print(root.xml_doc())
    pass


def xml4h_test2():
    xml4h.write_node = override_write_node
    root = xml4h.build('root') \
            .e('level1') \
                .e('level2').t('text') \
                .up() \
                .e('level2').t('">="') \
                .up() \
            .up()
        # .up()
    print(root.xml_doc())
    pass


def lxml_test():
    root = etree.Element('root')
    level1 = etree.SubElement(root, 'level1')
    level2 = etree.SubElement(level1, 'level2')
    level2.text = 'text'
    level2 = etree.SubElement(level1, 'level2')
    level2.text = '">="'
    print(etree.tostring(root, method='xml', pretty_print=True))
    pass


if __name__ == '__main__':
    xml4h_test1()
    xml4h_test2()
    lxml_test()
    pass
