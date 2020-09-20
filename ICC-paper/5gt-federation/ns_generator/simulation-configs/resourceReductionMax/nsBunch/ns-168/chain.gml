graph [
  node [
    id 0
    label 1
    disk 1
    cpu 1
    memory 10
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 3
    memory 11
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 1
    memory 16
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 3
    memory 4
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 4
    memory 2
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 1
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 127
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 162
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 180
  ]
  edge [
    source 2
    target 3
    delay 32
    bw 68
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 123
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 181
  ]
]
