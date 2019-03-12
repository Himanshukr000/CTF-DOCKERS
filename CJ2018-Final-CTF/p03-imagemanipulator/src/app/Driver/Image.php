<?php

class Image
{
    /**
     * Calculates a lighter (or darker) version of a color.
     *
     * @param string $color    An HTML color, e.g.: #ffffcc.
     * @param integer $factor  The brightness difference between -0xff and
     *                         +0xff. Plus values raise the brightness,
     *                         negative values reduce it.
     *
     * @return string  A modified HTML color.
     */
    public static function modifyColor($color, $factor = 0x11)
    {
        list($r, $g, $b) = self::getColor($color);

        $r = min(max($r + $factor, 0), 255);
        $g = min(max($g + $factor, 0), 255);
        $b = min(max($b + $factor, 0), 255);

        return '#' . str_pad(dechex($r), 2, '0', STR_PAD_LEFT)
            . str_pad(dechex($g), 2, '0', STR_PAD_LEFT)
            . str_pad(dechex($b), 2, '0', STR_PAD_LEFT);
    }

    /**
     * Calculates a more intense version of a color.
     *
     * @param string $color    An HTML color, e.g.: #ffffcc.
     * @param integer $factor  The intensity difference between -0xff and
     *                         +0xff. Plus values raise the intensity,
     *                         negative values reduce it.
     *
     * @return string  A more intense HTML color.
     */
    public static function moreIntenseColor($color, $factor = 0x11)
    {
        list($r, $g, $b) = self::getColor($color);

        if ($r >= $g && $r >= $b) {
            $g = $g / $r;
            $b = $b / $r;

            $r += $factor;
            $g = floor($g * $r);
            $b = floor($b * $r);
        } elseif ($g >= $r && $g >= $b) {
            $r = $r / $g;
            $b = $b / $g;

            $g += $factor;
            $r = floor($r * $g);
            $b = floor($b * $g);
        } else {
            $r = $r / $b;
            $g = $g / $b;

            $b += $factor;
            $r = floor($r * $b);
            $g = floor($g * $b);
        }

        $r = min(max($r, 0), 255);
        $g = min(max($g, 0), 255);
        $b = min(max($b, 0), 255);

        return '#' . str_pad(dechex($r), 2, '0', STR_PAD_LEFT)
            . str_pad(dechex($g), 2, '0', STR_PAD_LEFT)
            . str_pad(dechex($b), 2, '0', STR_PAD_LEFT);
    }

    /**
     * Returns the brightness of a color.
     *
     * @param string $color  An HTML color, e.g.: #ffffcc.
     *
     * @return integer  The brightness on a scale of 0 to 255.
     */
    public static function brightness($color)
    {
        list($r, $g, $b) = self::getColor($color);
        return round((($r * 299) + ($g * 587) + ($b * 114)) / 1000);
    }

    /**
     * Calculates the grayscale value of a color.
     *
     * @param integer $r  A red value.
     * @param integer $g  A green value.
     * @param integer $b  A blue value.
     *
     * @return integer  The grayscale value of the color.
     */
    public static function grayscaleValue($r, $g, $b)
    {
        return round(($r * 0.30) + ($g * 0.59) + ($b * 0.11));
    }

    /**
     * Turns an RGB value into grayscale.
     *
     * @param integer[] $originalPixel  A hash with 'red', 'green', and 'blue'
     *                                  values.
     *
     * @return integer[]  A hash with 'red', 'green', and 'blue' values for the
     *                    corresponding gray color.
     */
    public static function grayscalePixel($originalPixel)
    {
        $gray = self::grayscaleValue(
            $originalPixel['red'],
            $originalPixel['green'],
            $originalPixel['blue']
        );
        return array('red' => $gray, 'green' => $gray, 'blue' => $gray);
    }

    /**
     * Normalizes an HTML color.
     *
     * @param string $color  An HTML color, e.g.: #ffffcc or #ffc.
     *
     * @return integer[]  Array with three elements: red, green, and blue.
     */
    public static function getColor($color)
    {
        if ($color[0] == '#') {
            $color = substr($color, 1);
        }

        if (strlen($color) == 3) {
            $color = str_repeat($color[0], 2) .
                str_repeat($color[1], 2) .
                str_repeat($color[2], 2);
        }

        return array(
            hexdec(substr($color, 0, 2)),
            hexdec(substr($color, 2, 2)),
            hexdec(substr($color, 4, 2))
        );
    }
    /**
     * Returns an x,y pair on circle, assuming center is 0,0.
     *
     * @param float $degrees     The degrees of arc to get the point for.
     * @param integer $diameter  The diameter of the circle.
     *
     * @return array  (x coordinate, y coordinate) of the point.
     */
    public static function circlePoint($degrees, $diameter)
    {
        // Avoid problems with floats.
        $degrees += 0.0001;

        return array(cos(deg2rad($degrees)) * ($diameter / 2),
                     sin(deg2rad($degrees)) * ($diameter / 2));
    }

    /**
     * Returns point coordinates at the limits of an arc.
     *
     * @param integer $r      The radius of the arc.
     * @param integer $start  The starting angle.
     * @param integer $end    The ending angle.
     *
     * @return array  The start point (x1,y1), end point (x2,y2), and anchor
     *                point (x3,y3).
     */
    public static function arcPoints($r, $start, $end)
    {
        // Start point.
        $pts['x1'] = $r * cos(deg2rad($start));
        $pts['y1'] = $r * sin(deg2rad($start));

        // End point.
        $pts['x2'] = $r * cos(deg2rad($end));
        $pts['y2'] = $r * sin(deg2rad($end));

        // Anchor point.
        $pts['x3'] = $pts['y3'] = 0;

        // Shift to positive.
        if ($pts['x1'] < 0) {
            $pts['x2'] += abs($pts['x1']);
            $pts['x3'] += abs($pts['x1']);
            $pts['x1'] = 0;
        }
        if ($pts['x2'] < 0) {
            $pts['x1'] += abs($pts['x2']);
            $pts['x3'] += abs($pts['x2']);
            $pts['x2'] = 0;
        }
        if ($pts['x3'] < 0) {
            $pts['x1'] += abs($pts['x3']);
            $pts['x2'] += abs($pts['x3']);
            $pts['x3'] = 0;
        }
        if ($pts['y1'] < 0) {
            $pts['y2'] += abs($pts['y1']);
            $pts['y3'] += abs($pts['y1']);
            $pts['y1'] = 0;
        }
        if ($pts['y2'] < 0) {
            $pts['y1'] += abs($pts['y2']);
            $pts['y3'] += abs($pts['y2']);
            $pts['y2'] = 0;
        }
        if ($pts['y3'] < 0) {
            $pts['y1'] += abs($pts['y3']);
            $pts['y2'] += abs($pts['y3']);
            $pts['y3'] = 0;
        }

        return $pts;
    }

    /**
     * Returns the point size for an HTML font size name.
     */
    public static function getFontSize($fontsize)
    {
        switch ($fontsize) {
        case 'medium':
            return 18;
        case 'large':
            return 24;
        case 'giant':
            return 30;
        default:
            return 12;
        }
    }

}
