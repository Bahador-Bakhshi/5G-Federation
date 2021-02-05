graph [
  node [
    id 0
    label 1
    disk 4
    cpu 4
    memory 3
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 3
    memory 14
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 2
    memory 7
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 3
    memory 8
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 4
    memory 13
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 143
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 180
  ]
  edge [
    source 0
    target 2
    delay 25
    bw 144
  ]
  edge [
    source 0
    target 3
    delay 28
    bw 185
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 142
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 66
  ]
  edge [
    source 3
    target 4
    delay 25
    bw 127
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 144
  ]
]
