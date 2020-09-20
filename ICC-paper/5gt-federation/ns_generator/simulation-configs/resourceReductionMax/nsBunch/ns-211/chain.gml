graph [
  node [
    id 0
    label 1
    disk 8
    cpu 1
    memory 2
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 1
    memory 16
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 3
    memory 1
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 3
    memory 6
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 3
    memory 6
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 1
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 175
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 188
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 168
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 55
  ]
  edge [
    source 1
    target 4
    delay 25
    bw 138
  ]
  edge [
    source 2
    target 4
    delay 29
    bw 153
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 182
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 89
  ]
]
