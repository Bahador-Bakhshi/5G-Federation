graph [
  node [
    id 0
    label 1
    disk 1
    cpu 3
    memory 14
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 4
    memory 16
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 1
    memory 8
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 2
    memory 3
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 2
    memory 9
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 2
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 162
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 168
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 69
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 200
  ]
  edge [
    source 3
    target 4
    delay 32
    bw 99
  ]
  edge [
    source 3
    target 5
    delay 29
    bw 116
  ]
]
