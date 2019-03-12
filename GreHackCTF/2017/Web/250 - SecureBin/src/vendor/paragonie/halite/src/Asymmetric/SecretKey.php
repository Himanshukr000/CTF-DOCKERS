<?php
namespace ParagonIE\Halite\Asymmetric;

use ParagonIE\Halite\HiddenString;
use ParagonIE\Halite\Key;
use ParagonIE\Halite\Alerts\CannotPerformOperation;

/**
 * Class SecretKey
 * @package ParagonIE\Halite\Asymmetric
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */
class SecretKey extends Key
{
    /**
     * @param HiddenString $keyMaterial - The actual key data
     */
    public function __construct(HiddenString $keyMaterial)
    {
        parent::__construct($keyMaterial);
        $this->isAsymmetricKey = true;
    }
    
    /**
     * See the appropriate derived class.
     * @throws CannotPerformOperation
     * @return void
     */
    public function derivePublicKey()
    {
        throw new CannotPerformOperation(
            'This is not implemented in the base class'
        );
    }
}
