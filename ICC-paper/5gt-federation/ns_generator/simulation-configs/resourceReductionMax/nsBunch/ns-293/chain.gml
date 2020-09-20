graph [
  node [
    id 0
    label 1
    disk 1
    cpu 1
    memory 13
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 2
    memory 6
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 2
    memory 13
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 3
    memory 9
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 1
    memory 6
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 1
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 175
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 144
  ]
  edge [
    source 1
    target 2
    delay 29
    bw 174
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 150
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 168
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 142
  ]
]
