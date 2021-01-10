from __future__ import annotations
from typing import Any, Optional


class Node(object):
    def __init__(self, data: Any, next_node: Node = None, prev_node: Node = None) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublylinkedList(object):

    def __init__(self, head: Node = None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> Node:
        current_node = self.head
        # データが1つ（先頭のみdataが存在する場合）
        if current_node and current_node.data == data:
            if current_node.next is None:
                current_node = None
                self.head = None
                return
            else:
                next_node = current_node.next
                next_node.prev = None
                current_node = None
                self.head = next_node
                return

        # データが１つ以上の指定したデータを削除する場合
        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None:
            return

        # データが１つ以上の一番最後尾のデータを削除する場合
        if current_node.next is None:
            prev = current_node.prev
            prev.next = None
            current_node = None
            return
        else:
            next_node = current_node.next
            prev_node = current_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None
            return

    def reverse_iterative(self) -> None:
        previous_node = None
        current_node = self.head
        while current_node:
            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node

            current_node = current_node.prev

        if previous_node:
            self.head = previous_node.prev

    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: None) -> Optional[Node]:
            if not current_node:
                return None

            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node

            if current_node.prev is None:
                return current_node

            return _reverse_recursive(current_node.prev)

        self.head = _reverse_recursive(self.head)

    def sort(self) -> None:
        if self.head is None:
            return

        current_node = self.head
        # 1, 5, 2, 9
        # 1
        while current_node.next:
            # 5
            next_node = current_node.next
            # 5, 2, 9
            while next_node:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = next_node.data, current_node.data
                next_node = next_node.next

            current_node = current_node.next


if __name__ == '__main__':
    d = DoublylinkedList()
    d.append(1)
    d.append(5)
    d.append(2)
    d.append(9)

    d.print()

    print("######## Reverse Iter")
    d.reverse_iterative()
    d.print()

    d.reverse_iterative()

    print("######## Reverse Rec")
    d.reverse_recursive()
    d.print()
    d.reverse_recursive()

    print("######## Sort")
    d.sort()
    d.print()














