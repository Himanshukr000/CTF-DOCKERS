<?php
declare(strict_types=1);

namespace ParagonIE\EasyDB\Tests;

use ParagonIE\EasyDB\EasyDB;
use ParagonIE\EasyDB\Factory;
use PHPUnit_Framework_TestCase;

/**
 * Class EasyDBTest
 * @package ParagonIE\EasyDB\Tests
 */
abstract class EasyDBTest extends PHPUnit_Framework_TestCase
{

    /**
    * Data provider for arguments to be passed to Factory::create
    * These arguments will not result in a valid EasyDB instance
    * @return array
    */
    public function BadFactoryCreateArgumentProvider()
    {
        return [
            [
                'this-dsn-will-fail',
                'username',
                'putastrongpasswordhere'
            ],
        ];
    }

    /**
    * Data provider for arguments to be passed to Factory::create
    * These arguments will result in a valid EasyDB instance
    * @return array
    */
    public function GoodFactoryCreateArgumentProvider()
    {
        switch (getenv('DB')) {
            case false:
                return [
                    [
                        'sqlite::memory:',
                        null,
                        null,
                        [],
                        'sqlite'
                    ],
                ];
            break;
        }
        $this->markTestIncomplete(
            'Could not determine appropriate arguments for ' .
            Factory::class .
            '::create() from getenv()'
        );
        return [];
    }

    /**
    * EasyDB data provider
    * Returns an array of callables that return instances of EasyDB
    * @return array
    * @see EasyDBTest::GoodFactoryCreateArgumentProvider()
    */
    public function GoodFactoryCreateArgument2EasyDBProvider()
    {
        return array_map(
            function (array $arguments) {
                $dsn = $arguments[0];
                $username = isset($arguments[1]) ? $arguments[1] : null;
                $password = isset($arguments[2]) ? $arguments[2] : null;
                $options = isset($arguments[3]) ? $arguments[3] : [];
                return [
                    function () use ($dsn, $username, $password, $options) {
                        return Factory::create(
                            $dsn,
                            $username,
                            $password,
                            $options
                        );
                    }
                ];
            },
            $this->GoodFactoryCreateArgumentProvider()
        );
    }

    /**
    * Strict-type paranoia for a callable that is expected to return an EasyDB instance
    * @param callable $cb
    * @return EasyDB
    */
    protected function EasyDBExpectedFromCallable(callable $cb) : EasyDB
    {
        return $cb();
    }

    /**
    * Remaps EasyDBWriteTest::GoodFactoryCreateArgument2EasyDBProvider()
    */
    public function GoodFactoryCreateArgument2EasyDBQuoteProvider()
    {
        $cbArgsSets = $this->GoodFactoryCreateArgument2EasyDBProvider();
        $args = [
            [
                1,
                [
                    "'1'"
                ]
            ],
            [
                '1foo',
                [
                    "'1foo'"
                ]
            ]
        ];

        return array_reduce(
            $args,
            function (array $was, array $is) use ($cbArgsSets) {
                foreach ($cbArgsSets as $cbArgs) {
                    $args = array_values($is);
                    foreach (array_reverse($cbArgs) as $cbArg) {
                        array_unshift($args, $cbArg);
                    }
                    $was[] = $args;
                }

                return $was;
            },
            []
        );
    }
}
