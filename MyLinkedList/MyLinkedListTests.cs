using System;
using System.Collections.Generic;
using FluentAssertions;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace BrainTrain.MyLinkedList
{
    [TestClass]
    public class MyLinkedListTests
    {
        [TestMethod]
        public void WhenAddFirst_FirstIsReturned()
        {
            // Arrange
            var node = new MyLinkedListNode<int>();
            var sut = new MyLinkedList<int>();

            // Act
            sut.AddFirst(node);

            // Assert
            sut.First.Should().Be(node);
        }

        [TestMethod]
        public void WhenAddFirst_LastIsReturned()
        {
            // Arrange
            var node = new MyLinkedListNode<int>();
            var sut = new MyLinkedList<int>();

            // Act
            sut.AddFirst(node);

            // Assert
            sut.Last.Should().Be(node);
        }

        [TestMethod]
        public void AddAfter_WhenNodeIsNull_ThrowArgumentNullException()
        {
            // Arrange
            var sut = new MyLinkedList<int>();

            // Act
            var action = new Action(()=> sut.AddAfter(null, new MyLinkedListNode<int>() ));

            // Assert
            action.Should().Throw<ArgumentNullException>().WithMessage("Value cannot be null. (Parameter 'node')");
        }

        [TestMethod]
        public void AddAfter_WhenNewNodeIsNull_ThrowArgumentNullException()
        {
            // Arrange
            var sut = new MyLinkedList<int>();

            // Act
            var action = new Action(() => sut.AddAfter( new MyLinkedListNode<int>(), null));

            // Assert
            action.Should().Throw<ArgumentNullException>().WithMessage("Value cannot be null. (Parameter 'newNode')");
        }

        [TestMethod]
        public void AddAfter_()
        {
            // Arrange
            var firstNode = new MyLinkedListNode<int>();
            var secondNode = new MyLinkedListNode<int>();
            var sut = new MyLinkedList<int>();

            sut.AddFirst(firstNode);

            // Act
            sut.AddAfter(firstNode, secondNode);

            // Assert
            sut.First.Should().Be(firstNode);
        }

        [TestMethod]
        public void test()
        {
            var a = new LinkedList<int>();

            
        }
    }

    public class MyLinkedListNode<T>
    {
    }
}