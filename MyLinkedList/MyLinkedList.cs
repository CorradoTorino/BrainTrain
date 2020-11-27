using System;

namespace BrainTrain.MyLinkedList
{
    public class MyLinkedList<T>
    {
        private MyLinkedListNode<T> first = null;

        public void AddFirst(MyLinkedListNode<T> node)
        {
            this.first = node;
        }

        public MyLinkedListNode<T> First => first;

        public MyLinkedListNode<T> Last {
            get { return first; }
        }

        public void AddAfter(MyLinkedListNode<T> node, MyLinkedListNode<T> newNode)
        {
            if ( node == null)
            {
                throw new ArgumentNullException(nameof(node));
            }

            if (newNode == null)
            {
                throw new ArgumentNullException(nameof(newNode));
            }

        }
    }
}
