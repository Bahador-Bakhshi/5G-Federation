graph [
  node [
    id 0
    label 1
    disk 1
    cpu 2
    memory 11
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 3
    memory 14
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 2
    memory 10
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 2
    memory 14
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 4
    memory 3
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 152
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 87
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 171
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 148
  ]
  edge [
    source 2
    target 3
    delay 32
    bw 155
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 104
  ]
  edge [
    source 4
    target 5
    delay 25
    bw 88
  ]
]
