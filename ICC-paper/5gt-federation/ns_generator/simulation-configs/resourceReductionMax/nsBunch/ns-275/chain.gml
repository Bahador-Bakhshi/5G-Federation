graph [
  node [
    id 0
    label 1
    disk 3
    cpu 4
    memory 9
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 2
    memory 1
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 2
    memory 12
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 3
    memory 3
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 1
    memory 10
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 3
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 111
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 124
  ]
  edge [
    source 1
    target 2
    delay 33
    bw 68
  ]
  edge [
    source 1
    target 3
    delay 26
    bw 167
  ]
  edge [
    source 1
    target 4
    delay 33
    bw 117
  ]
  edge [
    source 2
    target 5
    delay 25
    bw 76
  ]
  edge [
    source 3
    target 5
    delay 31
    bw 183
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 147
  ]
]
