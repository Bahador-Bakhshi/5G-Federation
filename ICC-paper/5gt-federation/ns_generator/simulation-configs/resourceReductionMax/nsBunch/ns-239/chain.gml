graph [
  node [
    id 0
    label 1
    disk 5
    cpu 3
    memory 4
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 1
    memory 14
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 4
    memory 6
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 1
    memory 11
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 4
    memory 5
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 4
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 54
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 52
  ]
  edge [
    source 1
    target 2
    delay 25
    bw 153
  ]
  edge [
    source 2
    target 3
    delay 31
    bw 189
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 162
  ]
  edge [
    source 3
    target 5
    delay 32
    bw 111
  ]
]
