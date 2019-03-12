<?php
declare(strict_types=1);

namespace ParagonIE\EasyDB\Tests;

use InvalidArgumentException;

class UpdateTest extends
        EasyDBWriteTest
{

    /**
     * @dataProvider GoodFactoryCreateArgument2EasyDBProvider
     * @param callable $cb
     */
    public function testUpdateArgChangesReturnsNull(callable $cb)
    {
        $db = $this->EasyDBExpectedFromCallable($cb);
        $this->assertEquals(
            $db->update('irrelevant_but_valid_tablename', [], ['1=1']),
            null
        );
    }

    /**
     * @dataProvider GoodFactoryCreateArgument2EasyDBProvider
     * @param callable $cb
     */
    public function testUpdateArgConditionsReturnsNull(callable $cb)
    {
        $db = $this->EasyDBExpectedFromCallable($cb);
        $this->assertEquals(
            $db->update('irrelevant_but_valid_tablename', ['foo' => 'bar'], []),
            null
        );
    }

    /**
     * @dataProvider GoodFactoryCreateArgument2EasyDBProvider
     * @param callable $cb
     */
    public function testUpdateArgChangesThrowsException(callable $cb)
    {
        $db = $this->EasyDBExpectedFromCallable($cb);
        $this->expectException(InvalidArgumentException::class);
        $db->update('irrelevant_but_valid_tablename', [[1]], ['TRUE' => true]);
    }

    /**
     * @dataProvider GoodFactoryCreateArgument2EasyDBProvider
     * @param callable $cb
     */
    public function testUpdateArgConditionsThrowsException(callable $cb)
    {
        $db = $this->EasyDBExpectedFromCallable($cb);
        $this->expectException(InvalidArgumentException::class);
        $db->update('irrelevant_but_valid_tablename', ['1=1'], [[1]]);
    }

    /**
     * @dataProvider GoodFactoryCreateArgument2EasyDBProvider
     * @param callable $cb
     */
    public function testUpdateTableNameThrowsException(callable $cb)
    {
        $db = $this->EasyDBExpectedFromCallable($cb);
        $this->expectException(InvalidArgumentException::class);
        $db->update('', ['foo' => 'bar'], ['TRUE' => true]);
    }

    /**
     * @dataProvider GoodFactoryCreateArgument2EasyDBProvider
     * @param callable $cb
     */
    public function testUpdateArgChangesKeyThrowsException(callable $cb)
    {
        $db = $this->EasyDBExpectedFromCallable($cb);
        $this->expectException(InvalidArgumentException::class);
        $db->update('irrelevant_but_valid_tablename', ['1foo' => 1], ['TRUE' => true]);
    }

    /**
     * @dataProvider GoodFactoryCreateArgument2EasyDBProvider
     * @param callable $cb
     */
    public function testUpdateArgConditionsKeyThrowsException(callable $cb)
    {
        $db = $this->EasyDBExpectedFromCallable($cb);
        $this->expectException(InvalidArgumentException::class);
        $db->update('irrelevant_but_valid_tablename', ['foo' => 1], ['1foo' => true]);
    }

    /**
     * @dataProvider GoodFactoryCreateArgument2EasyDBProvider
     * @depends      ParagonIE\EasyDB\Tests\InsertManyTest::testInsertMany
     * @param callable $cb
     */
    public function testUpdate(callable $cb)
    {
        $db = $this->EasyDBExpectedFromCallable($cb);
        $db->insertMany('irrelevant_but_valid_tablename', [['foo' => '1'], ['foo' => '2']]);
        $this->assertEquals(
            $db->single('SELECT COUNT(*) FROM irrelevant_but_valid_tablename'),
            2
        );
        $this->assertEquals(
            $db->single('SELECT COUNT(*) FROM irrelevant_but_valid_tablename WHERE foo = ?', [1]),
            1
        );
        $this->assertEquals(
            $db->single('SELECT COUNT(*) FROM irrelevant_but_valid_tablename WHERE foo = ?', [2]),
            1
        );
        $this->assertEquals(
            $db->single('SELECT COUNT(*) FROM irrelevant_but_valid_tablename WHERE foo = ?', [3]),
            0
        );
        $db->update('irrelevant_but_valid_tablename', ['foo' => 3], ['foo' => 2]);
        $this->assertEquals(
            $db->single('SELECT COUNT(*) FROM irrelevant_but_valid_tablename WHERE foo = ?', [2]),
            0
        );
        $this->assertEquals(
            $db->single('SELECT COUNT(*) FROM irrelevant_but_valid_tablename WHERE foo = ?', [3]),
            1
        );
    }
}
