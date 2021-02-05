graph [
  node [
    id 0
    label 1
    disk 3
    cpu 4
    memory 13
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 2
    memory 10
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 4
    memory 5
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 3
    memory 13
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 4
    memory 15
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 4
    memory 7
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 136
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 109
  ]
  edge [
    source 0
    target 2
    delay 25
    bw 160
  ]
  edge [
    source 0
    target 3
    delay 26
    bw 161
  ]
  edge [
    source 1
    target 5
    delay 35
    bw 107
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 79
  ]
  edge [
    source 3
    target 4
    delay 25
    bw 125
  ]
  edge [
    source 4
    target 5
    delay 25
    bw 128
  ]
]
